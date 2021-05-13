import math
while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s)/n
    numerator = sum([(float(s[i])-m)**2 for i in range(n)])
    alphalpha = numerator / n
    print("{0:.8f}".format(math.sqrt(alphalpha)))