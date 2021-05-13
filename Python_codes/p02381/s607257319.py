import math

for i in range(1000):
    
    n=float(input())
    if n==0:
        break
    
    s= list(map(float, input().split()))
    m=sum(s)/n
    
    X=[]
    n=int(n)
    for j in range (n):
        x=(s[j]-m)**2
        X.append(x)
    a=math.sqrt(sum(X)/n)
    print(f'{a:.08f}')
