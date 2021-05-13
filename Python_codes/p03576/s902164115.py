
N,K = map(int,input().split())

xy = []
xlis = []
ylis = []

for i in range(N):

    x,y = map(int,input().split())

    xy.append([x,y])

    if x not in xlis:
        xlis.append(x)
    if y not in ylis:
        ylis.append(y)

ans = float("inf")
xlis.sort()
ylis.sort()

for rp in range(len(xlis)):

    right = xlis[rp]

    for lp in range(rp+1):

        left = xlis[lp]

        for upp in range(len(ylis)):

            up = ylis[upp]

            for dp in range(upp+1):

                down = ylis[dp]

                able = 0
                nable = 0
                for i in range(N):

                    nx = xy[i][0]
                    ny = xy[i][1]
                    if left <= nx and nx <= right and down <= ny and ny <= up:
                        able += 1
                    else:
                        nable += 1

                    if able >= K or nable > N-K:
                        break

                if able >= K:
                    now = max(1,right-left) * max(1,up-down)
                    ans = min(ans,now)

print (ans)
