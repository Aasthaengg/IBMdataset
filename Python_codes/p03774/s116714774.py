n, m = map(int, input().split())
N = [list(map(int, input().split())) for _ in range(n)]
M = [list(map(int, input().split())) for _ in range(m)]


for i in range(n):
    ans = 0
    d = 9999999999999999999999
    for j in range(m):
        tmp = abs(N[i][0]-M[j][0]) + abs(N[i][1]-M[j][1])
        if tmp < d:
            d = tmp
            ans = j
    print(ans+1)