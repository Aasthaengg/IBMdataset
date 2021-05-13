N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    a, b = AB[i]
    x = abs(CD[0][0]-a)+abs(CD[0][1]-b)
    y = 0
    for j in range(1, M):
        c, d = CD[j]
        ky = abs(c-a)+abs(d-b)
        if ky < x:
            x = ky
            y = j
    print(y+1)