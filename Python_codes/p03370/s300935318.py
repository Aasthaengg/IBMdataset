n,m=map(int,input().split());count=0
l=[int(input()) for _ in range(n)]
r=sum(l);count=len(l)
while r<=m-min(l):
  r+=min(l)
  count+=1
print(count)