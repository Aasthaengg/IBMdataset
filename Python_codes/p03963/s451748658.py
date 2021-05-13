N, K = map(int, input().split())

# 最初の一回目はKパターン
ans = K
for i in range(1,N):
    if K-1>0:
        ans *= K-1
print(ans)