n,a,b,c = map(int,input().split())
L = []
for i in range(n):
    L.append(int(input()))
import itertools
ans = 10**9
tmp = 0
for use in itertools.product([0,1,2,-1] ,repeat=n):
    tmp = 0
    ls = [0,0,0]
    for idx,u in enumerate(use):
        if u>-1:
            if ls[u] >0:
                tmp+=10
            ls[u]+=L[idx]

    if ls[0] ==0 or ls[1] ==0 or ls[2] ==0:continue
    tmp = tmp + abs(ls[0] -a) +abs(ls[1] -b)+abs(ls[2] -c)
    ans = min(tmp,ans)
print(ans)
