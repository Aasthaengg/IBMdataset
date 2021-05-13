MOD=1000000007
N=int(input())
d = {}
pairs=[-1]*N

for i in range(N):
    c = int(input())
    if c in d and i-d[c]>1:
        pairs[d[c]] = i
    d[c]=i
    
dp1,dp2=[0]*N,[0]*N
prev=1
for src in range(N):
    dp2[src]=(prev+dp1[src])%MOD
    dst = pairs[src]
    if dst>0:
        dp1[dst] = (dp1[dst]+dp2[src])%MOD
    prev=dp2[src]
print(dp2[-1])
