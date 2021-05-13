n = int(input())
ans = 0
now = -1
for i in range(n):
  a,b = map(int,input().split())
  if a > now:
    now = a
    ans = a + b

print(ans)