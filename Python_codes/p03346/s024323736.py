N = int(input())
P = [int(input()) for i in range(N)]
is_earlier = [True] * N
appeared = set()
appeared.add(N+1)
for p in P:
  if p+1 in appeared:
    is_earlier[p-1] = False
  appeared.add(p)

M = 0
now = 1
for i in range(N):
    if is_earlier[i]:
        now += 1
    else:
        M = max(M, now)
        now = 1

print(N - M)