N, K, Q = map(int, input().split())
s = []
[s.append(K-Q) for _ in range(N)]
for _ in range(Q):
  n = int(input())
  s[n-1] += 1
for t in s:
  if t > 0:
    print('Yes')
  else:
    print('No')