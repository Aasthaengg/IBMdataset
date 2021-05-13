n=int(input())
l=list(map(int,input().split()))
if(n==1):
    print("Yes")
else:
    f=0
    for i in range(n-1,-1,-1):
        if(l[i]+1==l[i-1]):
            l[i-1]-=1
    for i in range(n-1):
        if(l[i+1]<l[i]):
            f=1
            break

    if(f==0):
        print("Yes")
    else:
        print("No")
