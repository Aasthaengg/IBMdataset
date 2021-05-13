d,n=map(int,input().split())
a=[100**d*i for i in range(n+1)]
if d==0 and n==100:
    print(101)
elif d==1 and n==100:
    print(10100)
elif d==2 and n==100:
    print(1010000)
else:
    print(a[-1])