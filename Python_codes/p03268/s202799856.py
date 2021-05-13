n,k=map(int,input().split())

if k%2==1:
    q= n//k 
    print(q**3);exit()
q=n//k 

qq=len([i for i in range(k//2,n+1,k)])
print(q**3+qq**3)