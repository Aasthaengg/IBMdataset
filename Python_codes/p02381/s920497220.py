import math
while True:
    n = int(input())
    if n == 0: break
    s = tuple(map(int, input().split()))
    su = sum(s)
    m = sum(s) / n
    print(math.sqrt(sum([(si - m)**2 for si in s])/float(n)))