import math
while True:
    n=input()
    if n==0: break
    s=map(int,raw_input().split())
    mean=float(sum(s))/len(s)
    var=[(x-mean)**2/n for x in s]
    print math.sqrt(sum(var))