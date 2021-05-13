import sys

n=int(input())
a=list(map(int,input().split()))

#n=5
#a=[2,4,4,0,2]

#n=7
#a=[6,4,0,2,4,0,2]

#n=8
#a=[7,5,1,1,7,3,5,3]

acnt=[0]*n

for i in range(n):
    acnt[a[i]]=acnt[a[i]]+1
    
mod=10**9+7   
if n%2==0:
    for i in range(1,n,2):
        if acnt[i]!=2:
            print(0)
            sys.exit()
    print(pow(2,n//2,mod))
elif n%2==1:
    if acnt[0]!=1:
        print(0)
    else:
        for i in range(2,n,2):
            if acnt[i]!=2:
                print(0)
                sys.exit()
        print(pow(2,n//2,mod))
