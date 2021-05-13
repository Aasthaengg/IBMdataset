n=int(input())
if n==1:
    print(1)
else:
    l1=2
    l2=1
    for i in range(n-1):
        l3=l1+l2
        l1=l2
        l2=l3
    print(l2)