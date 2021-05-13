from itertools import accumulate

n, c = (int(x) for x in input().split())
X = []
V = []
D = []
prev_x = 0
for _ in range(n):
    x, v = (int(x) for x in input().split())
    X.append(x)
    D.append(x - prev_x)
    V.append(v)
    prev_x = x
D.append(c - X[-1])
rev_D = list(reversed(D))
rev_V = list(reversed(V))

ans = 0
# 時計回り
A = [0] * n
for i in range(n):
    A[i] = V[i] - D[i]
acc_A = list(accumulate(A))
ans = max(ans, max(acc_A))

# 反時計回り
B = [0] * n
for i in range(n):
    B[i] = rev_V[i] - rev_D[i]
acc_B = list(accumulate(B))
ans = max(ans, max(acc_B))

max_acc_A = [acc_A[0]]
max_acc_B = [acc_B[0]]
for i in range(1, n):
    max_acc_A.append(max(max_acc_A[-1], acc_A[i]))
    max_acc_B.append(max(max_acc_B[-1], acc_B[i]))

# 時計回りからの反時計回り i個まで食べて向きを変える
tmp = 0
for i in range(n - 1):
    tmp_cal = acc_A[i] - X[i]  # 食べて原点まで戻った時点のカロリー
    tmp = max(tmp, tmp_cal + max_acc_B[n - i - 2])
ans = max(ans, tmp)

# 反時計回りからの時計回り
tmp = 0
for i in range(n - 1):
    tmp_cal = acc_B[i] - (c - X[-i - 1])  # 食べて原点まで戻った時点のカロリー
    tmp = max(tmp, tmp_cal + max_acc_A[n - i - 2])
ans = max(ans, tmp)

print(ans)
