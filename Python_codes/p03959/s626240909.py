MOD = 10 ** 9 + 7
n = int(input())
tlst = list(map(int, input().split()))
alst = list(map(int, input().split()))
cand_t = [[1, 1] for _ in range(n)]
cand_t[0] = [tlst[0], tlst[0]]
for i in range(1, n):
    if tlst[i] == tlst[i - 1]:
        cand_t[i][1] = tlst[i]
    else:
        cand_t[i] = [tlst[i], tlst[i]]
cand_a = [[1, 1] for _ in range(n)]
cand_a[-1] = [alst[-1], alst[-1]]
for i in range(n - 2, -1, -1):
    if alst[i] == alst[i + 1]:
        cand_a[i][1] = alst[i]
    else:
        cand_a[i] = [alst[i], alst[i]]
ans = 1
for (t_r, t_h), (a_r, a_h) in zip(cand_t, cand_a):
    r = max(t_r, a_r)
    h = min(t_h, a_h)
    if r > h:
        print(0)
        break
    ans *= (h - r + 1)
    ans %= MOD
else:
    print(ans)