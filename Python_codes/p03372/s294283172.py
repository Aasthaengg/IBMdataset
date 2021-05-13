N, C = map(int, input().split())
x = []
v = []
for _ in range(N):
    xi, vi = map(int, input().split())
    x.append(xi)
    v.append(vi)
vsp = [0] * (N + 1)
vsn = [0] * (N + 1)
dprp = [0] * (N + 1)
dprn = [0] * (N + 1)
dpsp = [0] * (N + 1)
dpsn = [0] * (N + 1)
for i in range(N):
    vsp[i + 1] = vsp[i] + v[i]
    vsn[i + 1] = vsn[i] + v[N - 1 - i]
    dprp[i + 1] = max(dprp[i], vsp[i + 1] - 2 * x[i])
    dpsp[i + 1] = max(dpsp[i], vsp[i + 1] - x[i])
    dprn[i + 1] = max(dprn[i], vsn[i + 1] - 2 * (C - x[N - 1 - i]))
    dpsn[i + 1] = max(dpsn[i], vsn[i + 1] - (C - x[N - 1 - i]))
ans = max([max(dprp[i] + dpsn[N - i], dprn[i] + dpsp[N - i])
           for i in range(N + 1)])
print(ans)
