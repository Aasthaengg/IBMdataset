
import numpy as np

dic={}
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

A = input()
for a in ascii_lowercase:
    dic[a]=[0]*len(A)

i=0
for l in A:
    dic[l][i]=1
    i+=1

for d in dic:
    dic[d]=np.cumsum(dic[d])



dp=[0]*len(A)
dp[0]=1
for i in range(1,len(A)):
    tmp = (i+1-dic[A[i]][i])
    #print(tmp)
    dp[i]=dp[i-1]+tmp

print(dp[-1])
