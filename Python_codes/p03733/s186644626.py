N, T = map(int, input().split())
t_list = list(map(int, input().split()))

diff_t = [t_list[i+1] - t_list[i] for i in range(N-1)]

ans = 0
for dt in diff_t:
    if dt <= T:
        ans += dt
    else:
        ans += T

ans += T
print(ans)