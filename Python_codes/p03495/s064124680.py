from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
c = Counter(A)
d = c.most_common()

ans = N
for i in range(K):
  if i == len(d):
    break
  ans -= d[i][1]
print(ans)