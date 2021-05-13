r,d,a=map(int,input().split())
for i in range(1,11):
    print(int(a*(r**i)-d*(r**i-1)/(r-1)))