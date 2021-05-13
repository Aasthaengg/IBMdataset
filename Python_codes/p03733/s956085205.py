N, T = map(int, input().split())
t_list = list(map(int, input().split()))
ans = 0
pre_ti = 0
for i in range(1, N):
    ti = t_list[i]
    ans += min(T, ti-pre_ti)
    pre_ti = ti
ans += T
print(ans)