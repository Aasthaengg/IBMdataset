n, k = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(n)]
L = sorted(L, key=lambda x: x[0])
s = 0
i = 0
while s < k:
    s += L[i][1]
    i += 1
print(L[i-1][0])
