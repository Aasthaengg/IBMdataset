n = int(input())
P = list(map(int, input().split()))
S = [i for i in range(1, n + 1)]
ans = "YES"
if P != S:
  ans = "NO"
  for i in range(n):
    for j in range(i + 1, n):
      P[i], P[j] = P[j], P[i]
      if P == S:
        ans = "YES"
        break
      P[i], P[j] = P[j], P[i]
print(ans)