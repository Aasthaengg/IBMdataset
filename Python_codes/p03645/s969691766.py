N, M = map(int, input().split())

s = set()
g = set()

for _ in range(M):
    A, B = map(int, input().split())
    if A == 1:
        s.add(B)
    if B == N:
        g.add(A)

if s & g:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

