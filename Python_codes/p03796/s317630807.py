MOD = pow(10,9)+7
N = int(input())
now = 1
for i in range(1,N+1):
  now = now*i%MOD
print(now)