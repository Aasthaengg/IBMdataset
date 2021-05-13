N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

minw = min(w)
for i in range(N):
    w[i] -= minw

ww = [[] for _ in range(4)]
for i, o in enumerate(w):
    ww[o].append(v[i])
for i in range(4):
    ww[i].sort(reverse=True)

ans = 0
for i in range(len(ww[0])+1):
    isum = sum(ww[0][:i])
    for j in range(len(ww[1])+1):
        jsum = sum(ww[1][:j])
        for k in range(len(ww[2])+1):
            ksum = sum(ww[2][:k])
            for t in range(len(ww[3])+1):
                tsum = sum(ww[3][:t])
                weight = minw * i + (minw+1) * j + (minw+2) * k + (minw+3) * t
                if weight <= W:
                    ans = max(ans, isum+jsum+ksum+tsum)
print(ans)
