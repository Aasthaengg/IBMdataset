F = [1, 1]
for i in range(7):
  F.append(F[i]+F[i+1])

h, w, k = map(int, input().split())
mod = 10**9 + 7
a = [[0 for i in range(w)] for i in range(h+1)]
a[0][0] = 1

if w == 1:
  print(1)
else:
  for i in range(h):
    for j in range(w):
      if j == 0:
        a[i+1][j] += F[w-1] * a[i][j] % mod
        a[i+1][j+1] += F[w-2] * a[i][j] % mod
      elif j==w-1:
        a[i+1][j] += F[w-1] * a[i][j] % mod
        a[i+1][j-1] += F[w-2] * a[i][j] % mod
      else:
        a[i+1][j] += F[j] * F[w-j-1] * a[i][j] % mod
        a[i+1][j+1] += F[j] * F[w-j-2] * a[i][j] % mod
        a[i+1][j-1] += F[j-1] * F[w-j-1] * a[i][j] % mod
        
  print(a[-1][k-1]%mod)