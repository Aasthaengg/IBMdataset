import math
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

D = [x for i in range(4)]

for i in range(len(D)):
    if i == len(D) -1:
        D[i] = 0
        for j in range(n):
            di = math.fabs(x[j]-y[j])
            if D[i] < di:
                D[i] = di

    else:
        p = 1
        p += i
        di = 0
        d = 0
        for k in range(n):
            d += math.fabs(x[k]-y[k])**p
        di = d**(1/p)
        D[i] = di

for i in range(len(D)):
    print(D[i])