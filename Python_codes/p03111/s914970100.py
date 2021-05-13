n,a,b,c = map(int,input().split())
L = []
for i in range(n):
    L.append(int(input()))
import itertools
ans = 10**9
tmp = 0
for perm in itertools.permutations(range(n),3):
    ua,ub,uc = perm
    la,lb,lc = L[ua],L[ub],L[uc]
    for use in itertools.product([0,1,2,-1] ,repeat=n-3):
        idx = 0
        tmp = 0
        ls = [la,lb,lc]
        for i,l in enumerate(L):
            if i== ua or  i== ub or i== uc:
                continue
            else:
                if use[idx]>-1:
                    ls[use[idx]] +=l
                    tmp+=10
            idx+=1
        tmp = tmp + abs(ls[0] -a) +abs(ls[1] -b)+abs(ls[2] -c)
        ans=min(ans,tmp)
print(ans)
