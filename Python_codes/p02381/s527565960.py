import math
while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    x=0
    m=sum(s)/n
    for i in s:
        x+=(i-m)**2
    print(math.sqrt(x/n))

