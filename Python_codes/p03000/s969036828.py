n,x = map(int,input().split())
L = list(map(int,input().split()))
y = 0
ans = 0
for i in range(n):
  if y<=x:
    ans+=1
  y+=L[i]

if y<=x:
  ans+=1
print(ans)