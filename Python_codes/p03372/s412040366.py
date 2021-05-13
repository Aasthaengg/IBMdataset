N, C = map(int, input().split())

# x = 0 に v = 0 の寿司があると考える
X = [0]
V = [0]

for _ in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)

# 0, v_1, v_1+v_2, v_1+v_2+v_3, ...
cumsum1 = [0]
for i in range(1, N + 1):
    cumsum1.append(cumsum1[-1] + V[i])

# 0, v_N, v_N+v_N-1, v_N+v_N-1+v_N-2, ...
cumsum2 = [0]
for i in range(N, 0, -1):
    cumsum2.append(cumsum2[-1] + V[i])

# 歩く範囲を弧ABと考える(A<=B)
# x_A = 0, x_1, x_2, ..., x_N
# x_B = x_A, ..., x_N

# 0, v_1-x_1, v_1+v_2-x_2, v_1+v_2+v_3-x_3, ...
f1 = [0]
# 0, v_1-2*x_1, v_1+v_2-2*x_2, v_1+v_2+v_3-2*x_3, ...
f2 = [0]
for i in range(1, N + 1):
    f1.append(cumsum1[i] - X[i])
    f2.append(cumsum1[i] - 2 * X[i])

f1_max = [0]
for i in range(1, N + 1):
    f1_max.append(max(f1_max[-1], f1[i]))
f2_max = [0]
for i in range(1, N + 1):
    f2_max.append(max(f2_max[-1], f2[i]))

ans = 0
# Bを全探索（固定する）
for i in range(N + 1):
    if i == 0:
        continue
    else:
        # 0 -> B(反時計回り、反転なし)
        ans = max(ans, cumsum1[i] - X[i])
        # 0 -> B(時計回り、反転なし)
        ans = max(ans, cumsum2[N + 1 - i] - (C - X[i]))
        # 0 -> A -> B(反転)
        ans = max(ans, f2_max[i - 1] + cumsum2[N + 1 - i] - (C - X[i]))
        # 0 -> B -> A(反転)
        ans = max(ans, f1_max[i - 1] + cumsum2[N + 1 - i] - 2 * (C - X[i]))

print(ans)
