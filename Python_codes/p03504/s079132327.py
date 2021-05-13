N, C = map(int, input().split())
accu = [[0]*(10**5+10) for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    accu[c-1][s] += 1
    accu[c-1][t+1] -= 1
for i in range(C):
    for j in range(1, 10**5+10):
        accu[i][j] += accu[i][j-1]
ans = 0
for i in range(10**5+10):
    tmp = 0
    for j in range(C):
        tmp += accu[j][i]>0
    ans = max(ans, tmp)
print(ans)