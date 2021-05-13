import math
while True:
    n=int(input())
    if n == 0: break
    x=list(map(int,input().split()))
    ave=sum(x)/n
    a=0
    for i in x:
        a += (i-ave)**2 / n
    print(math.sqrt(a))