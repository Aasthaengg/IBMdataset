A, B, M = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = min(P) + min(Q)
for i in range(M):
  x, y, c = map(int, input().split())
  ans = min(ans, P[x-1]+Q[y-1]-c)
print(ans)