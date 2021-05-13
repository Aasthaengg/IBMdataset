N, K = map(int, input().split())
A = list(map(int, input().split()))

# imos法して，もう一回同じことを行う
# K回のシミューレション，途中で全てがKになったら打ち切る
for _ in range(K):
    new = [0] * N
    imos = [0] * N
    for i, a in enumerate(A):  # 0-indexにしても問題ない
        imos[max(0, i-a)] += 1
        if i+a+1 <= N-1:  # 右端まで照らすなら，終端は管理しない
            imos[i+a+1] -= 1
    for i in range(N):
        new[i] = new[i-1] + imos[i]
    # Aを上書き
    A = new
    if sum(A) == N*N:
        break
print(*A)
