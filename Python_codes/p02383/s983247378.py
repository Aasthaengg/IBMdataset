n1,n2,n3,n4,n5,n6=map(int,raw_input().split())
act=raw_input()
for i in act:
    if i=="N":
        n11=n1
        n1=n2
        n2=n6
        n6=n5
        n5=n11
    elif i=="S":
        n11=n1
        n1=n5
        n5=n6
        n6=n2
        n2=n11
    elif i=="E":
        n11=n1
        n1=n4
        n4=n6
        n6=n3
        n3=n11
    else :
        n11=n1
        n1=n3
        n3=n6
        n6=n4
        n4=n11
print(n1)