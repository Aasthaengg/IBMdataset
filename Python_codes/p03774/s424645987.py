N, M = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]
c = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    m = 0
    for j in range(M):
        if abs(s[i][0]-c[m][0]) + abs(s[i][1]-c[m][1]) > abs(s[i][0]-c[j][0]) + abs(s[i][1]-c[j][1]):
            m = j
    print(m+1)
