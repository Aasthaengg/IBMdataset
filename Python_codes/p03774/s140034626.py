N,M = map(int, input().split())
S = [list(map(int,input().split())) for _ in range(N)]
C = [list(map(int,input().split())) for _ in range(M)]
for a, b in S:
    distance = 1001001001
    ans = 0
    for i in range(len(C)):
        c, d = C[i][0], C[i][1]
        if abs(a - c) + abs(b - d) < distance:
            distance = abs(a - c) + abs(b - d)
            ans = i + 1
    print(ans)
