h = int(input())
w = int(input())
n = int(input())

ans = 0
max = max(h, w)
while n > 0:
  n -= max
  ans += 1

print(ans)