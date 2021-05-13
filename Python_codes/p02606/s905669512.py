l, r, d = map(int, input().split())

ans = r // d - l // d
if l % d == 0:
  ans += 1

print(ans)