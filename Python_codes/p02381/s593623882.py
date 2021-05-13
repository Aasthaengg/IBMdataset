import math
while True:
    n=int(input())
    if n==0:
        break
    
    lis=list(map(int,input().split()))
    m=sum(lis)/n
    s=0
    for i in range(n):
        s+=(lis[i]-m)*(lis[i]-m)
    a=math.sqrt(s/n)
    print("{:10f}".format(a))
    
