import math
while True:
    a=[]
    n=int(input())
    if n==0:
        break
    c=0
    a=list(map(int,input().split()))
    ave=sum(a)/len(a)
    for i in range(n):
        c=c+(a[i]-ave)**2
    print('{:.10f}'.format(math.sqrt(c/n)))
        
