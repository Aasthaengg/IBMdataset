n, k = map(int, input().split())
D = 10**9 + 7

up = [1] * (n + 1)
down = [0] * (n + 1)
for i in range(1, n + 1):
  up[i] = (up[i - 1] * i) % D
down[n] = pow(up[n], D - 2, D)
for i in range(n, 0, -1):
  down[i - 1] = (down[i] * i) % D
  
def cmd(n, r, D):
  if r < 0 or r > n:
    return 0
  else:
    return (up[n] * down[r] * down[n - r]) % D

A = 0
k = min(k, n-1)
t = 0
while t <=k:
  A = (A + cmd(n-1, t, D) * cmd(n, t, D)) % D
  t = t+1
print (A)