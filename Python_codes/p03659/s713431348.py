N = int(input())
a = list(map(int, input().split()))

x = [0] * (N+1)

for i in range(1, N+1):
  x[i] = x[i-1] + a[i-1]

suma = x[N]
y = [suma] * (N+1)
for i in range(1, N+1):
  y[i] = y[i-1] - a[i-1]
  
ans = sum([abs(i) for i in a])
for i in range(1, N):
  ans = min(ans, abs(x[i]-y[i]))
  
print(ans)