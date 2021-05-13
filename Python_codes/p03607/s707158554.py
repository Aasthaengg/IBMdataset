n = int(input())
alst = [int(input()) for _ in range(n)]
alst.sort()
bef = -1
ans = 0
for a in alst:
  if a == bef:
    ans -= 1
    bef = -1
  else:
    ans += 1
    bef = a
print(ans)