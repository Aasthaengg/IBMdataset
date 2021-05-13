data = int(input())
modu = 10 ** 9 + 7
n = 1
for i in range(2, data + 1):
  n *= i
count = 1
ans = 1
for i in range(2, data + 1):
  if n % i != 0:
    continue
  count = 1
  while n % i == 0:
    n //= i
    count += 1
  ans *= count
print(ans % modu)