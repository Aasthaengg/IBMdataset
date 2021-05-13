import math
l, r = list(map(int, input().split()))

if (2019*math.ceil(l/2019) <= r):
    print(0)
else:
    minres = 2018

    for i in range(l, r+1):
        im = i % 2019
        for j in range(i+1, r+1):
            res = (im*(j%2019))%2019
            if res < minres:
                minres = res

    print(minres)