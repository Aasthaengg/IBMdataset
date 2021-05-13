n,p=map(int,input().split())
a=list(map(lambda x:int(x)%2,input().split()))
on=a.count(1)
ze=a.count(0)
ans=0
if on==0:
    if p==0:
        print(2**n)
        exit()
    if p==1:
        print(0)
        exit()
    
print(2**(n-1))