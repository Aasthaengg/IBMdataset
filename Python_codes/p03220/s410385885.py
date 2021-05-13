N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

pt = [abs(A - (T - h * 0.006)) for h in H]

# np.argsortなしで，最大値，最小値のindexを取得
ans = min(enumerate(pt), key=lambda x: x[1])[0]
print(ans + 1)

# 最大値が複数あるとき
# [i for i, v in enumerate(li) if v == max(l)]
# 計算重そう

