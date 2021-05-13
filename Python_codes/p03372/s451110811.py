N, C = map(int, input().split())
x = [0]
v = [0]
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    v.append(b)
opt_l = [0]
acc_v = 0
for i in range(1, N + 1):
    opt_l.append(max(opt_l[-1], v[i] + acc_v - x[i]))
    acc_v += v[i]
opt_r = [0]
acc_v = 0
for i in range(1, N + 1):
    opt_r.append(max(opt_r[-1], v[-i] + acc_v - (C - x[-i])))
    acc_v += v[-i]
ans = 0
acc_v = 0
for i in range(N + 1):
    ans = max(
        ans,
        acc_v + v[i] - x[i],
        acc_v + v[i] - 2 * x[i] + opt_r[N - i]
    )
    acc_v += v[i]
acc_v = 0
for i in range(N + 1):
    ans = max(
        ans,
        acc_v + v[-i] - (C - x[-i]),
        acc_v + v[-i] - 2 * (C - x[-i]) + opt_l[N - i]
    )
    acc_v += v[-i]
print(ans)