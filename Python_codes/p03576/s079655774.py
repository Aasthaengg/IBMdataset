

N,K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

Xs = set()
Ys = set()
for x,y in XY:
    Xs.add(x)
    Ys.add(y)


Xs = list(Xs)
Xs.sort()

Ys = list(Ys)
Ys.sort()

LX = len(Xs)
LY = len(Ys)
ans = 10**20

for i in range(LX):
    for j in range(i+1, LX):
        for k in range(LY):
            for l in range(k+1, LY):
                cnt = 0
                for x,y in XY:
                    if Xs[i] <= x <= Xs[j] and Ys[k] <= y <= Ys[l]:
                        cnt += 1

                if cnt >= K:
                    ans = min(ans, (Xs[j] - Xs[i])*(Ys[l] - Ys[k]))


print(ans)