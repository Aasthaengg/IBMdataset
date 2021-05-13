n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans=0
for a,b in ab:
  if m>=b:
    m-=b
    ans+=b*a
  else:
    ans+=a*m
    break
print(ans)
