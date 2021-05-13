import collections

N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
B = [0] * Q
C = [0] * Q
for i in range(Q):
  B[i], C[i] = [int(x) for x in input().split()]

count = collections.defaultdict(lambda: 0)
current = 0
for a in A:
  count[a] += 1
  current += a

for b, c in zip(B,C):
  current += (c - b) * count[b]
  print(current)
  count[c] += count[b]
  del count[b]
