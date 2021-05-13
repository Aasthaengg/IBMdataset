N,M = map(int, input().split())

tpls = []
for i in range(N):
    a,b = map(int, input().split())
    tpls.append((a, b))
tpls.sort()
need = 0
now = 0
idx = 0
while now < M:
    a, b = tpls[idx]
    if now + b > M:
        need += a * (M - now)
        now = M
    else:
        need += a*b
        now += b
    idx += 1
print(need)