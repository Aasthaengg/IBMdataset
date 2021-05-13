N=int(input())
c=0
ans=0
for x in range(N):
  p=int(input())
  if p>c:
    c=p
  ans+=p
print(ans-c//2)