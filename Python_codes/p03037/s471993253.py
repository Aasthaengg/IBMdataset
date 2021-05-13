N, M = map(int, input().split())
L = [0] * M
R = [0] * M
for c in range(M):
    L[c], R[c] = map(int, input().split())

L_max = max(L)
R_min = min(R)

ans = R_min - L_max
ans += 1

if ans < 0:
    print(0)
else:
    print(ans)