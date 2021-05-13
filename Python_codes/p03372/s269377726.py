N,C = map(int, input().split())
x = [0] * N
v = [0] * N
for i in range(N):
    x[i], v[i] = map(int, input().split())

x_cum_L = [0] * (N+1)
v_cum_L = [0] * (N+1)
x_cum_R = [0] * (N+1)
v_cum_R = [0] * (N+1)
for i in range(1, N+1):
    x_cum_L[i] = x[i-1]
    v_cum_L[i] = v_cum_L[i-1] + v[i-1]
    x_cum_R[i] = C - x[-i]
    v_cum_R[i] = v_cum_R[i-1] + v[-i]

reward_L = [0] * (N+1)
reward_R = [0] * (N+1)
for i in range(N+1):
    reward_L[i] = v_cum_L[i] - x_cum_L[i]
    reward_R[i] = v_cum_R[i] - x_cum_R[i]

reward_max_L = [0] * (N+1)
reward_max_R = [0] * (N+1)
for i in range(1, N+1):
    reward_max_L[i] = max(reward_max_L[i-1], reward_L[i])
    reward_max_R[i] = max(reward_max_R[i-1], reward_R[i])

ans = 0
for i in range(N+1):
    ans_L = reward_L[i] - x_cum_L[i] + reward_max_R[N - i]
    ans_R = reward_R[i] - x_cum_R[i] + reward_max_L[N - i]
    ans = max(ans, ans_L, ans_R)

print(ans)
