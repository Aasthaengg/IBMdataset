n = int(input())

res = 1
for i in range(1,n+1):
  res *= i
  res = res % (10**9+7)
print(res)