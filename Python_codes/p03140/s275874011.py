n = int(input())
a = input().strip()
b = input().strip()
c = input().strip()
ans = 0
for _a, _b, _c in zip(a, b, c):
  if _a != _b and _b != _c and _a != _c:
    ans += 2
  elif _a == _b and _b == _c:
    continue
  else:
    ans += 1
print(ans)