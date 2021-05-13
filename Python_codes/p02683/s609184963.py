from itertools import product

N, M, X = map(int, input().split())
inp = [list(map(int, input().split())) for _ in range(N)]

C, A = [], []
for i in range(N):
    C.append(inp[i][0])
    A.append(inp[i][1:])

#判定
z_A = list(zip(*A))
for i in range(M):
    if sum(z_A[i]) < X:
        print(-1)
        exit()

ans = sum(C)

for buy_bit in product(range(2), repeat=N):
    buy = 0
    tmp = 0
    skill = [0] * M
    for i in range(N):
        if buy_bit[i]:
            for j in range(M):
                skill[j] += A[i][j]
            buy += C[i]
    
    f = True
    for s in skill:
        if s < X:
            f = False
            break
    if f:
        ans = min(ans, buy)

print(ans)