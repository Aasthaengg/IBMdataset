while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    sum=0
    for i in range(x//3+1,n+1):
        for j in range((x-i)//2+1,i):
            if 0<x-i-j<j :   
                sum+=1
    print(int(sum))