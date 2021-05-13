import math
while True:
    n=int(input())
    if n==0: break
    l = list(map(int, input().split()))
    s=0
    for i in l:
        s+=((i-sum(l)/n)**2)
    print("{0:.8f}".format(math.sqrt(s/n)))