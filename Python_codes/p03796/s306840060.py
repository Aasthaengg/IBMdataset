n = int(input())
mod = 1000000007
p = 1
for i in range(1, n+1):
  p = p*i%mod
print(p)