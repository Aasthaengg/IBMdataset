n = int(input())
pwr = 1
for i in range(1,n+1):
  pwr *= i
  if pwr>10**9+7:
    pwr = pwr%(10**9+7)
print(pwr%(10**9+7))