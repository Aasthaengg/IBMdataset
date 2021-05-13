n = int(input())
k = int(input())
x = int(input())
y = int(input())

cost = 0
if 1 <= n <= 10000 and 1 <= k <= 10000 and 1 <= y < x <= 10000:
  if n > k:
    cost += x * k
    cost += y * (n - k)
  elif n <= k:
    cost += n * x
  
print(cost)