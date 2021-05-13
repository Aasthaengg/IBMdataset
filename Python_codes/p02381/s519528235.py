import math
while 1:
    n=int(input())
    if n == 0: break 
    ss=list(map(float,input().split()))
    a=sum(ss)/n
    s=(sum([ (s-a)**2 for s in ss ]) / n)**0.5
    print('{0:.6f}'.format(s))