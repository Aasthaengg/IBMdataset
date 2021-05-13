N = int(input())

d = [[0]*N for _ in range(N)]

def warshall_floyd(d):
    global SUM
    ans = 0
    aroad = set()
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j]>d[i][k] + d[k][j]:
                    return -1
                if d[i][j]==d[i][k]+d[k][j] and not (i==k or k==j):
                    aroad.add((min(i, j), max(i, j)))
    for i, j in list(aroad):
        ans -= d[i][j]
    return SUM+ans

SUM = 0
for i in range(N):
    As = list(map(int, input().split()))
    SUM += sum(As)
    for j in range(N):
        d[i][j] = As[j] 
SUM //= 2
print(warshall_floyd(d))