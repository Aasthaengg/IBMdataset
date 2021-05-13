def com(n, k):
  P = [1]
  for i in range(1, n + 1):
    P.append(P[i - 1] * i)
  return P[n] / P[n - k] / P[k]


N, A, B = list(map(int, input().split()))
v = list(map(int, input().split()))

v.sort(reverse = True)
su = 0
for i in range(A):
  su += v[i]

ac = 0
t = v[A - 1]
k = 100
for i in range(N):
  if v[i] == t:
    ac += 1
    k = min(k, i)

print(su / A)
if k == 0:
  ans = 0
  for i in range(A, min(B, ac) + 1):
    ans += com(ac, i)
  print(int(ans))
else:
  print(int(com(ac, A - k)))