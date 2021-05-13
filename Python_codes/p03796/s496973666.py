N = int(input())
res = 1
for i in range(1,N+1):
  res = res*i
  res = res % 1000000007
print(res)