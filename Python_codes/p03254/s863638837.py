N,x = map(int,input().split())
a = sorted([int(i) for i in input().split()])
ans = 0
for i in a:
  x -= i
  if x >= 0:
    ans += 1
  else:
    break
else:
  if x > 0:
    ans -= 1

print(ans)