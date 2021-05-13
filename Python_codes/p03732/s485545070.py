N, W = map(int, input().split())

w, v = map(int, input().split())

values = [[] for _ in range(4)]

values[0].append(v)

for _ in range(N-1):
    x, y = map(int, input().split())
    values[x-w].append(y)

n = [0]*4
for i in range(4):
    n[i] = len(values[i])
    values[i].sort(reverse=1)

ans = 0
ans0 = 0
ans1 = 0
ans2 = 0
for n0 in range(n[0]+1):
    if n0 > 0:
        ans0 += values[0][n0-1]
    if n0 * w > W:
        break
    for n1 in range(n[1]+1):
        if n1 > 0:
            ans1 += values[1][n1-1]
        else:
            ans1 = 0
        if n0 * w + n1 * (w+1) > W:
            break
        for n2 in range(n[2]+1):
            ww = n0 * w + n1 * (w+1) + n2 * (w+2)
            if n2 > 0:
                ans2 += values[2][n2-1]
            else:
                ans2 = 0
            if ww > W:
                break
            n3 = (W - ww) // (w+3)
            ans = max(ans, ans0+ans1+ans2+sum(values[3][:n3]))

print(ans)