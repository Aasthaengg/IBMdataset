# C - Attention

N = int(input())
S = list(str(input()))
e = 0
ecum = [0] * (N+1)
wcum = [0] * (N+1)
for i, s in enumerate(S):
    if s == 'E':
        e += 1
        ecum[i+1] = ecum[i] + 1
        wcum[i+1] = wcum[i]
    else:
        ecum[i+1] = ecum[i]
        wcum[i+1] = wcum[i] + 1

ans = 10**18
for i in range(1, N+1):
    # 自分より左にいる西を向いてる人＋右にいる東を向いてる人
    cost = wcum[i-1] + (e - ecum[i])
    ans = min(ans, cost)
print(ans)