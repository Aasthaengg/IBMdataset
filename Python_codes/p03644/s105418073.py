n = int(input())
for i in range(7):
  c = 2**i
  if c > n:
    c //= 2
    break
print(c)