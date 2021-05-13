n, k = map(int, input().split())
P = [*map(lambda x: int(x)-1, input().split())]
C = [*map(int, input().split())]

score = -10**18
for st in range(n):
    lap_sc = sum_sc = 0
    nx = st
    for lap_cn in range(1, n+1):
        lap_sc += C[nx]
        nx = P[nx]
        if nx == st: break
    lap_sc = max(0, lap_sc)

    for k_cn in range(1, k+1):
        sum_sc += C[nx]
        score = max(score, sum_sc + lap_sc * ((k - k_cn) // lap_cn))
        nx = P[nx]
        if nx == st: break

print(score)
