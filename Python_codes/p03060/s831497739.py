n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
ans=0

for (p,q) in zip(x,y):
  if p-q>0:
    ans+=p-q
print(ans)