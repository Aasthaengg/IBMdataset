import sys
a=list(map(int,input().split()))
a.sort()
l0=a[0]-a[2]
l1=a[1]-a[2]
l2=0
c=0
while(c<1000):
    if l2==l1 and l2==l0:
        print(c)
        break
    elif l1==l0:
        l1+=1
        l0+=1
    elif (l1-l0)%2==0:
        l0+=2
    else:
        l0+=1
        l2+=1
    c+=1