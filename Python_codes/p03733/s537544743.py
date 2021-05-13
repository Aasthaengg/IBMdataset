N, T = map(int, input().split())
t = list(map(int, input().split()))
ans_t = T

for i in range(1, N):
    if t[i] <= t[i - 1] + T:
        ans_t = ans_t - t[i - 1] + t[i]
    else:
        ans_t += T

print(ans_t)