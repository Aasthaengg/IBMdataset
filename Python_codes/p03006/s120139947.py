N = int(input())
x, y = [], []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

res = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        p = x[i] - x[j]
        q = y[i] - y[j]
        
        cnt = 0
        for ii in range(N):
            for jj in range(N):
                pp = x[jj] - p
                qq = y[jj] - q
                if ii == jj:
                    continue
                if pp == x[ii] and qq == y[ii]:
                    cnt += 1
            res = max(res, cnt)

print(N - res)
