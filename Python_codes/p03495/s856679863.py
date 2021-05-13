N, K = map(int, input().split())
A = list(map(int, input().split()))
d = {}
for a in A:
  d[a] = d.get(a, 0) + 1
X = sorted(d.values(), reverse = True)
if len(X) <= K:
  print(0)
else:
  ans = N
  for i in range(K):
    ans -= X[i]
  print(ans)