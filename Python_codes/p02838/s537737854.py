N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
S0 = [0 for i in range(60)]
S1 = [0 for i in range(60)]
for i in range(N):
  for j in range(60):
    if A[i] % 2  == 0:
      S0[j] += 1
    else:
      S1[j] += 1
    A[i] //= 2
ans = 0
c = 1
for j in range(60):
  ans = (ans + S0[j] * S1[j] * c) % mod
  c *= 2
print(ans)