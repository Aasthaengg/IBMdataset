N, H = map(int,input().split())
L = []
maxi = 0
for _ in range(N):
    a,b = map(int,input().split())
    maxi = max(maxi, a)
    L.append((a,b))
cand = []
throw = 0
cnt = 0
for l in L:
    if maxi <  l[1]:
        throw += l[1]
        cand.append(l[1])
        cnt += 1
import math
if H - throw > 0: 
    print(math.ceil((H - throw)/maxi) + cnt )
else:
    throw = 0
    cnt = 0
    cand.sort()
    for x in cand[::-1]:
        throw += x
        cnt += 1
        if throw >= H:
            print(cnt)
            quit()

