N, M = map(int, input().split())

L = [None] * M
R = [None] * M

for i in range(M):
    l, r = map(int, input().split())
    L[i] = l
    R[i] = r

L_max = max(L)
R_min = min(R)

if L_max > R_min:
    print(0)
else:
    print(R_min - L_max + 1)
