import sys

A, B, C, D, E, F = map(int, sys.stdin.readline().rstrip().split())

q = [A, B]
water = []
while q:
    num = q.pop()
    if 100 * num <= F:
        water.append(num)
    else:
        continue
    q.append(num + A)
    q.append(num + B)

water = set(water)
w_ans = 0
s_ans = 0
nodo_ans = -1 # 濃度が0のときにも答えの更新が行われるようにする
V = [C, D]

for w in water:
    max_s = min(E * w, F - w * 100) # 溶かせる砂糖の量の最大値
    dp = [[0] * (max_s + 1) for _ in range(3)]
    dp[0][0] = 1
    for i in range(2):
        v = V[i]
        for j in range(max_s + 1):
            if j - v >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - v], dp[i + 1][j - v])
            else:
                dp[i + 1][j] = dp[i][j]

    for i, d in enumerate(dp[2]):
        if d > 0:
            nodo = i * 100 / (100 * w + i)
            if nodo_ans < nodo:
                s_ans = i
                w_ans = w * 100
                nodo_ans = nodo

print(w_ans + s_ans, s_ans)