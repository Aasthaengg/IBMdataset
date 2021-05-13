X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)

ab = []
for a in A:
  for b in B:
    ab += [a+b]
ab = sorted(ab, reverse=True)
ab = ab[:X+Y+Z+1]

ans = []
for n in ab:
  for c in C:
    ans += [n+c]
ans = sorted(ans, reverse=True)
for i in range(K):
  print(ans[i])
