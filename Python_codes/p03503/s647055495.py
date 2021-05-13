N = int(input())
F = [[] for _ in range(N)]
P = [[] for _ in range(N)]
for i in range(N):
    F[i] = list(map(int,(input().split())))
for i in range(N):
    P[i] = list(map(int,(input().split())))

ans = []

# 全探査
K = 2 # 選択肢の数
M = 10 # 問題の個数
for i in range(K**M):
    TF=[0]*M

    for j in range(M):
        TF[M-j-1] = i % K
        i //= K
    
    benefit = 0
    if sum(TF) != 0:
        for j in range(N):
            c = 0
            for k in range(10):
                if TF[k] == 1 and F[j][k] == 1:
                    c += 1
            benefit += P[j][c]
        ans.append(benefit)

print(max(ans))
