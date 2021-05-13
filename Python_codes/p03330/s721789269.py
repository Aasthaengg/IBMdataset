import numpy as np
import itertools
import sys
input = sys.stdin.readline  #文字列入力では注意！

N,C = map(int,input().split())
D = np.array([list(map(int,input().split()))for _ in range(C)], dtype=np.int64)
c = np.array([list(map(int,input().split()))for _ in range(N)], dtype=np.int64)
c0 = np.zeros(C,dtype=np.int64)
c1 = np.zeros(C,dtype=np.int64)
c2 = np.zeros(C,dtype=np.int64)
for i in range(N):
    for j in range(N):
        if (i+j)%3 == 0:
            c0[c[i,j]-1] += 1
        if (i+j)%3 == 1:
            c1[c[i,j]-1] += 1
        if (i+j)%3 == 2:
            c2[c[i,j]-1] += 1
# c0~2はXの情報
lis = itertools.permutations(range(C),3)
ans = float("inf")
for l0,l1,l2 in lis:    # l0~2はYの情報
    tmp = np.sum(D[:,l0]*c0+D[:,l1]*c1+D[:,l2]*c2)
    ans = min(ans,tmp)
print(ans)
