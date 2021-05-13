N, T = map(int, input().split())
t_l = list(map(int, input().split()))

tn = 0
ans = T
for i in range(N):
    t = t_l[i] - tn
    if t <= T:
        ans += t
    else:
        ans += T
    tn = t_l[i]
print(ans)