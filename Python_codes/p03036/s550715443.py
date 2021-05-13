
r,d,x_2000=map(int,input().split())

def X(n):    
    if n == 1:return x_2000
    else:return r*X(n-1)-d
lis=[X(n) for n in range(2,12)]
[print(i) for i in lis]