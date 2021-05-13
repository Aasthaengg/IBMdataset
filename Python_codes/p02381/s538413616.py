import math
while True:
    x = []
    n = int(input())
    if n == 0:
        break
    x = input().split( )
    suu = [float(s) for s in x]
#    print(x)
    kota = float(0)
    for a in suu:
        kota += ((a-sum(suu)/n)**2)/n
    print(math.sqrt(kota))
