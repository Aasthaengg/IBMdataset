n=int(input())
if 0<=n<=100:
    sum=100000
    for i in range(n):
        sum=sum*1.05
        if sum%1000==0:
            pass
        else:
            sum=sum-(sum%1000)+1000
    print(int(sum))
    
