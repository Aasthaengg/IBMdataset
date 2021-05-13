N,K=map(int,input().split())
if K%2==1:
    print((N//K)**3)
else:
    x=N//(K//2)
    odd=(x+1)//2
    even=x//2
    print(odd**3+even**3)
