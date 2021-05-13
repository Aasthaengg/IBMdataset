n,k=map(int,input().split())

if k==0:
    print(n**2)
else:
    #bの値かな
    co=0
    for i in range(k+1,n+1):
        co+=(n//i)*(i-k)
        co+=max(n%i-k+1,0)
    print(co)
