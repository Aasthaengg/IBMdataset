N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7

ans = 0
count=[0]*60
for a in A:
  for i in range(60):
    count[i] += a & 1
    a >>= 1
    
for i in range(60):
  ans += count[i] * (N - count[i]) * (2 ** i)
  ans %= mod
print(ans)
