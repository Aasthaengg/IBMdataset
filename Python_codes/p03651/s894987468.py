n, k = map(int, input().split())
A = sorted(map(int, input().split()))
INF = 10**9+1
diff = INF
for x, y in zip(A, A[1:]):
    z = abs(x-y)
    if z > 0:
        diff = min(diff, z)

MAX = A[-1]
ans = False
for a in A:
    if a-k < 0:
        continue
    x, r = divmod((a-k), diff)
    if r == 0:
        ans = True
        break
print("POSSIBLE" if ans else "IMPOSSIBLE")
