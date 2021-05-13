N, M, X = map(int, input().split())

INF = 30
ans = 1 << INF

data = []
for i in range(N):
    c = list(map(int, input().split()))
    data.append(c)

for i in range(1, 2**N):
    tmp = 0
    skill = [0] * M
    for j in range(N):
        if i >> j & 1:
            tmp += data[j][0]
            for k in range(M):
                skill[k] += data[j][k + 1]
    if min(skill) >= X and tmp < ans:
        ans = tmp

if ans == 1 << INF:
    print('-1')
else:
    print(ans)
