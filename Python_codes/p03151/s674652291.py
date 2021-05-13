import numpy as np

n = int(input())
a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))

d = a - b
s = np.sum(d)


if(s < 0):
    print(-1)
else:
    d = np.sort(d)
    d = d[d != 0]
    d2 = np.copy(d)
    i = -1
    for j in range(len(d2)):
        if(d2[j] >= 0):break
        while(d2[j] < 0):
            t = min(-d2[j],d2[i])
            d2[j] += t
            d2[i] -= t
            if(d2[i] == 0):i -= 1
    c = 0
    for i in range(len(d2)):
        if(d[i] != d2[i]):c += 1
    print(c)