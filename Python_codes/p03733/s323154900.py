si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))

# ----------

N, T = mii()
t = lmii()

p = []
t.sort()

st = t[0]
ed = t[0] + T
for i in range(1, N):
    n_st = t[i]
    n_ed = n_st + T

    if st <= n_st <= ed:
        ed = n_ed
    else:
        p.append((st, ed))
        st, ed = n_st, n_ed

p.append((st, ed))

ans = 0
for st, ed in p:
    ans += ed - st

print(ans)

