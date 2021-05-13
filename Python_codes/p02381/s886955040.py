import math

while True:
    n = int(input())
    if n == 0:
        break
    sn = [int(s) for s in input().split()]
    m = sum(sn) / n
    a2 = 0.0
    for s in sn:
        a2 += pow(s-m, 2)
    print(math.sqrt(a2/n))