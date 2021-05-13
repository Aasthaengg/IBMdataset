l1,l2=map(str,input().split(' '))
r,b=map(int,input().split(' '))
find=input()

if find==l1:
    r-=1
else:
    b-=1
print(r,b)