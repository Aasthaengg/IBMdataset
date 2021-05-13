N,L=map(int,input().split())
v=[L+i for i in range(N)]
s=sum(v)
ans=10**9
for i in range(N):
    if abs(s-(s-v[i]))<abs(s-ans):
        ans=s-v[i]
print(ans)