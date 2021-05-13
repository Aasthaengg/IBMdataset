import math
while True:
    n = int(input())
    if n==0: break
    s = list(map(int,input().split()))
    m = sum(s)/float(n)
    print("{0:.8f}".format(math.sqrt(sum([(x-m)**2 for x in s])/n)))