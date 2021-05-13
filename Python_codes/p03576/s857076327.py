n,bod = map(int,input().split())
points = []
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    points.append([a,b])

x.sort()
y.sort()


ans = 1e20

for i in range(n):
    for j in range(1,n-i):
        for k in range(n):
            for l in range(1,n-k):
                lef = x[i]
                rig = x[-j]
                bot = y[k]
                top = y[-l]

                cnt = 0
                for m in range(n):
                    if lef <= points[m][0] <= rig and bot <= points[m][1] <= top:
                        cnt += 1
                if cnt >= bod:
                    area = (rig-lef)*(top-bot)
                    if area < ans:
                        ans = area


print(ans)