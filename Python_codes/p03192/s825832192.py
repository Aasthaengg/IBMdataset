n = int(input())
k = 0
while n:
  if n % 10 == 2:
    k += 1
  n //= 10
print(k)