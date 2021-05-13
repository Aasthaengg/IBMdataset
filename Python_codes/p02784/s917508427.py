total,n=map(int,input().split(' '))
l1=list(map(int,input().split()))
s=sum(l1)
if(total==s or (total-s)<=0 ):
    print("Yes")
else:
    print("No")