a,b = map(int,input().split())
ans = 0
if a == 1:
  ans += 300000
elif a == 2:
  ans += 200000
elif a == 3:
  ans += 100000

if b == 1:
  ans += 300000
elif b == 2:
  ans += 200000
elif b == 3:
  ans += 100000

if a == 1 and b == 1:
  ans += 400000

print(ans)