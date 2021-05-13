N,T=map(int,input().split())
t=list(map(int,input().split()))
t.append(t[N-1]+T)
ans=0

for i in range(N):
    if t[i+1]-t[i]<=T:
        ans+=t[i+1]-t[i]
    else:
        ans+=T

print(ans)    