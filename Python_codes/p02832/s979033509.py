N = int(input())
A = list(map(int,input().split()))
target = 1
ans = 0
for i in A:
  if i==target:
    ans+=1
    target+=1
if not ans:
  print(-1)
else:
  print(N-ans)
