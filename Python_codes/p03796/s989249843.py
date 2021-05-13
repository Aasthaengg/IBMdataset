n = int(input())
p = 1
for i in range(1, n + 1):
  p *= i 
  if p >= 1000000007:
    p = p % 1000000007
print(p % 1000000007)