import math

while True:
    n = input()
    if n == 0:
        break
    s = map(int,raw_input().split())
    a2 = 0
    m = sum(s)/float(n)
    for i in s:
        a2 += (i - m)**2
    a2 = a2/float(n)
    print math.sqrt(a2)