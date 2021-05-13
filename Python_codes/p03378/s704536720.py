n,m,x = map(int,input().split())
a = list(map(int,input().split()))
s = len(a)
ans = 0
for i in a:
  if i < x:
    ans+=1
print(min(ans,s-ans))