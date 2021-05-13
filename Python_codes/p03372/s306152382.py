N, C = map(int, input().split())

xv = []
for i in range(N):
    x,v = map(int, input().split())
    xv.append((x,v))

fa = [0] * N
fa[0] = xv[0][1] - xv[0][0]
fb = [0] * N
fb[0] = xv[-1][1] - (C - xv[-1][0])
for i in range(1,N):
    fa[i] = fa[i-1] + xv[i][1] + xv[i-1][0] - xv[i][0]
    fb[i] = fb[i-1] + xv[N-1-i][1] + (C - xv[N-i][0]) - (C - xv[N-1-i][0])


max_fa = [0] * (N+1)
max_fa[0] = 0
max_fa[1] = max(0,fa[0])
max_fb = [0] * (N+1)
max_fb[0] = 0
max_fb[1] = max(0,fb[0])
for i in range(2,N+1):
    max_fa[i] = max(max_fa[i-1], fa[i-1])
    max_fb[i] = max(max_fb[i-1], fb[i-1])

ans_a = ans_b = 0

for i in range(N):
    ans_a = max(ans_a, max_fa[N-1-i] + fb[i] - (C - xv[N-1-i][0]) )
    ans_b = max(ans_b, max_fb[N-1-i] + fa[i] - xv[i][0])

ans_a = max(ans_a, max_fa[-1]) # xbがスタート地点の時
ans_b = max(ans_b, max_fb[-1]) # xaがスタート地点の時
print(max(ans_a, ans_b))
