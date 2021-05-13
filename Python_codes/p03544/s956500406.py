n=int(input())
l0=2
l1=1
l2=0
if n==0:
    print(2)
    exit()
if n==1:
    print(1)
    exit()
    
for i in range(2,n+1):
    l2=l1+l0
    l0=l1
    l1=l2
print(l2)    