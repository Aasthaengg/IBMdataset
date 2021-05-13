n=int(input())
f=[]
P=[]
for i in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(n):
    a=list(map(int, input().split()))
    P.append(a)
from itertools import product
ans=-(10**10)
for p in product([0, 1], repeat = 10):
    if sum(p)!=0:
        ret = 0
        for i in range(n):
            cnt = 0
            for j in range(10):
                if p[j] == f[i][j] and p[j] == 1:
                    cnt += 1
            ret += P[i][cnt]
        ans = max(ans, ret)
print(ans)