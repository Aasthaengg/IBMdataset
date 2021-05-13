a, b, x = list(map(int, input().split()))
c = b // x - a // x
if a % x == 0:
  c += 1
print(c)