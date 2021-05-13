mycode = r'''
# distutils: language=c++
# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True
ctypedef long long LL
# cython: cdivision=True
from libc.stdio cimport scanf
from libcpp.vector cimport vector
ctypedef vector[LL] vec
ctypedef vector[vec] vec_vec

cdef LL R,C,K,i,j,k

scanf("%lld %lld %lld",&R,&C,&K)

cdef vec_vec dp,ndp,item

dp = vec_vec(C,vec(3,0))
ndp = vec_vec(C,vec(3,0))
item = vec_vec(R,vec(C,0))


cdef LL r,c,v

for i in range(K):
    scanf("%lld %lld %lld",&r,&c,&v)
    item[r-1][c-1] = v

dp[C-1][0] = item[R-1][C-1]
dp[C-1][1] = item[R-1][C-1]
dp[C-1][2] = item[R-1][C-1]

for j in range(C-2,-1,-1):
    dp[j][0]=max(dp[j+1][1]+item[R-1][j],dp[j+1][0])
    dp[j][1]=max(dp[j+1][2]+item[R-1][j],dp[j+1][1])
    dp[j][2]=max(item[R-1][j],dp[j+1][2])

for i in range(R-2,-1,-1):
    ndp = vec_vec(C,vec(3,0))
    ndp[C-1][0]=dp[C-1][0]+item[i][C-1]
    ndp[C-1][1]=dp[C-1][0]+item[i][C-1]
    ndp[C-1][2]=dp[C-1][0]+item[i][C-1]
    for j in range(C-2,-1,-1):
        ndp[j][0]=max(max(dp[j][0],ndp[j+1][1])+item[i][j],ndp[j+1][0])
        ndp[j][1]=max(max(dp[j][0],ndp[j+1][2])+item[i][j],ndp[j+1][1])
        ndp[j][2]=max(dp[j][0]+item[i][j],ndp[j+1][2])
    dp=ndp

print(dp[0][0])

'''

import sys
import os
if sys.argv[-1] == 'ONLINE_JUDGE':  # コンパイル時
    with open('mycode.pyx', 'w') as f:
        f.write(mycode)
    os.system('cythonize -i -3 -b mycode.pyx')

import mycode
