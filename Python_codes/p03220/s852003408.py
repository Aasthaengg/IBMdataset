n=int(input())
t,a=map(int,input().split())
h=[t-int(x)*0.006 for x in input().split()]
ans=0
mn=10**18
for i,hi in enumerate(h):
  t=abs(hi-a)
  if t<mn:
    mn=t
    ans=i+1
print(ans)