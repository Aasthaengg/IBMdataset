from collections import defaultdict

N=int(input())
C=[int(input()) for _ in range(N)]

d = defaultdict(int)

ans=1
for i,c in enumerate(C):
    if i>=1 and C[i-1]==C[i]:
        continue
    else:
        ans+=d[c]
        d[c]=ans
        
        ans%=10**9+7
        d[c]%=10**9+7
print(ans)