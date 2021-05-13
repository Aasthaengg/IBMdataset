import math
while True:
    n = int(input())
    if n == 0:
        break
    s = [int(i) for i in input().split()]
    m = sum(s)/n
    a = [(s[i]-m)**2 for i in range(n)]
    v = sum(a)/n
    sb = math.sqrt(v)
    print("{:.5f}".format(sb))