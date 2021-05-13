from collections import defaultdict
d = defaultdict(int)

N, K = map(int, input().split())
A = list(map(int, input().split()))

inner = 0
for i in range(N):
  d[A[i]] += 1
  for j in range(i+1, N):
    if A[i] > A[j]:
      inner += 1
inner *= K

d = sorted(d.items())
outer = 0
cnt = d[0][1]
for k, v in d[1:]:
  outer += cnt * v
  cnt += v
outer *= K*(K-1)//2

print((inner + outer)%(10**9+7))