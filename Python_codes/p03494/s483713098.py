n=int(input())
a=list(map(int,input().split()))
i,c=0,0
while True:
    if a[i]%2==0:
        a[i]=a[i]/2
        i=i+1
    else:
        print(c)
        break
    if i==n-1:
        i=0
        c+=1