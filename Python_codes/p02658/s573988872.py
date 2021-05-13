n = int(input())
a = list(map(int, input().split()))
a.sort()
 
ans = 1
for x in a:
  if ans <= 10**18:
    ans = ans * x

print(-1 if ans > 10**18 else ans)
