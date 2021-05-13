N,X=map(int,input().split())
m=[int(input()) for _ in range(N)]
ans=0
m.sort()
X-=sum(m)
ans+=N
ans+=(X//m[0])
print(ans)