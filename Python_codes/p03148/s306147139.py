import heapq

N,K = map(int,input().split())

ans = 0

dt = []
maxt = 0

for i in range(N):

    t,d = map(int,input().split())

    dt.append([d,t])

    maxt = max(maxt,t)

dt.sort()
dt.reverse()

nsum = 0
nx = 0
uflag = [0] * (maxt+1)
up2mins = []
amari = []

for i in range(N):

    nt = dt[i][1]
    nd = dt[i][0]

    if i < K:

        nsum += nd

        if uflag[nt] == 0:
            uflag[nt] += 1
            nx += 1

        else:
            heapq.heappush(up2mins,nd)

    else:

        if uflag[nt] == 0:
            heapq.heappush(amari,-1 * nd)
            uflag[nt] += 1

ans = nsum + nx ** 2

#print (up2mins,amari,nsum,nx)

for i in range(N-K+1):

    if len(amari) == 0 or len(up2mins) == 0:
        break

    mnd = heapq.heappop(up2mins)

    pnd = -1 * heapq.heappop(amari)

    nx += 1

    nsum = nsum - mnd + pnd

    ans = max(ans , nsum + nx ** 2)


print (ans)
            

