N = int(input())
F = []
P = []
for i in range(N):
    F += [list(map(int, input().split()))]
for i in range(N):
    P += [list(map(int, input().split()))]
ans = float('-inf')

for b in range(2**10):
    tmp = 0
    sumc = 0
    for i in range(N):
        c = 0
        for j in range(10):
            if (b >> j) & 1 and F[i][j]:
                c += 1
        tmp += P[i][c]
        sumc += c
    if sumc:
        ans = max(ans, tmp)
print(ans)
