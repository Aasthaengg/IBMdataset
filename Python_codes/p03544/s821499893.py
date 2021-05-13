n=int(input())
l0=2
l1=1
if n>1:
    for i in range(2,n+1):
        l=l0+l1
        l0=l1
        l1=l
    print(l1)
elif n==1:
    print(1)
else:
    print(2)