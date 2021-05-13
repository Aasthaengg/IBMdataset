N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 最初のモンスター総数
mons_n = sum(A)

# 各勇者について
for i in range(N):
    # 余力
    power = B[i]
    # A[i]で出来る限り倒す時の撃破数
    temp = min(A[i], power)
    A[i] -= temp
    power -= temp

    # 余力でA[i+1]で限界まで戦う
    A[i + 1] -= min(A[i + 1], power)

print(mons_n - sum(A))
