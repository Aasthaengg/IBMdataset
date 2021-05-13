N, M = map(int, input().split())
L = 0
R = N+1
for _ in range(M):
    l, r = map(int, input().split())
    L = max(L, l)
    R = min(R, r)
print(R - L + 1 if R - L + 1 >= 0 else 0)
