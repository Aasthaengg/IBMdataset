n,a,b=map(int, input().split())
pot = b-a+1
if(b<a):
    print(0)
    exit()
if n==0:
    print(0)
elif n==1:
    if a==b:
        print(1)
    else:print(0)
elif n==2:
    if a==b:print(1)
    print(1)
else:
    k = n-1
    m = k*b
    high = m+a
    low = a*k + b
    print(high-low+1)
