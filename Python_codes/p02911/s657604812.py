N,K,Q = map(int, input().split())
D = {c:0 for c in range(1, N+1)}
for _ in range(Q):
  a = int(input())
  D[a] += 1
r = Q-K
for v in D.values():
  if v>r:
    print("Yes")
  else:
    print("No")