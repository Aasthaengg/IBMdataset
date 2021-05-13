N=int(input())
ans=0
l=0
for _ in range(N):
  p=int(input())
  ans+=p
  l=max(p,l)
print(ans-l//2)