l, h, d = map(int, input().split())
c = 0
for num in range(l, h+1):
  if num % d == 0:
    c += 1
print(c)