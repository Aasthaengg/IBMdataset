l = [int(x) for x in input().split()]
k, x = l[0], l[1]
a = max(-1000000, x - k + 1)
b = min(1000000, x + k - 1)
for x in range(a, b + 1):
  print(x, end=" ")
print()