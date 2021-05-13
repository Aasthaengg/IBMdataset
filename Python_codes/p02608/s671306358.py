from collections import defaultdict
n=int(input())
MAX=10001
RMAX=102
d = defaultdict(int)
for i in range(1,RMAX):
    wkx = i * i
    if wkx > MAX:
        break
    for j in range(1,RMAX):
        wky = wkx + j * j  + i * j
        if wky > MAX :
            break
        for k in range(1,RMAX):
            wkz = wky + k * k + i * k  + j * k
            if wkz > MAX :
                break
            d[wkz] += 1
            
for i in range(n):
    k = i + 1
    print(d[k])
