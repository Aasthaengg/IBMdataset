N, M = map(int, input().split())
A = []
for i in range(M):
  A += list(map(int, input().split()))
B = [0 for i in range(N)]
for a in A:
  B[a - 1] += 1
for b in B:
  print(b)