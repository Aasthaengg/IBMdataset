N, P = map(int, input().split())
S = input()

T = [0] * (N + 1)
T[0] = 0
e = 1
for i in range(N):
  T[i + 1] = T[i] + int(S[N - i - 1]) * e
  T[i + 1] %= P
  e *= 10
  e %= P

a = {}
for i in range(N + 1):
  if T[i] in a:
    a[T[i]] += 1
  else:
    a[T[i]] = 1

num = 0
if P % 2 == 0 or P % 5 == 0:
  for i in range(N):
    if int(S[i]) % P == 0:
      num += 1 + i
else:
  for k in a:
    num += a[k] * (a[k] - 1) // 2

print(num)