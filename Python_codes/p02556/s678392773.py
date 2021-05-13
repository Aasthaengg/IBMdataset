n=int(input())
a,b=[],[]
for _ in range(n):
  x,y=map(int,input().split())
  a+=(x+y),;b+=(x-y),
c=max(a)-min(a)
d=max(b)-min(b)
ans=max(c,d)
print(ans)