N, M = list(map(int, input().split()))
a = [int(input()) for _ in range(M)]
MOD = 10 ** 9 + 7
D = [0] * (N + 1)
D[0] = 1

a.append(10 ** 15)
c = 0
for i in range(1, N + 1):
  if a[c] == i:
    c += 1
    continue
  D[i] = D[i - 1]
  if i - 2 >= 0:
    D[i] = (D[i] + D[i - 2]) % MOD

print(D[-1])


