import math
while 1:
    n = int(input())
    if n == 0 :
        break
    a = list(map(int,input().split()))
    ave = sum(a)/n
    s = 0
    for i in range(n):
        s += (a[i] - ave)**2
    s2 = math.sqrt(s / n)
    print("%.9f"%s2)

