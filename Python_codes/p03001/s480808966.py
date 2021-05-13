W, H, x, y = map(int, input().split())
ans = W * H / 2
check = 0
if W / 2 == x and H / 2 == y:
  check = 1
print(ans, check)