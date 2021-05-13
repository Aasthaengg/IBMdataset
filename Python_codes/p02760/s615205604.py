a=[]
for i in range(3):
    x,y,z=map(int,input().split())
    a.append(x)
    a.append(y)
    a.append(z)
b=int(input())
for i in range(b):
    c=int(input())
    if a.count(c)==1:
        a[a.index(c)]=0
if a[0]==a[1]==a[2] or a[3]==a[4]==a[5] or a[6]==a[7]==a[8]:
    print("Yes")
elif a[0]==a[3]==a[6] or a[1]==a[4]==a[7] or a[2]==a[5]==a[8]:
    print("Yes")
elif a[0]==a[4]==a[8] or a[2]==a[4]==a[6]:
    print("Yes")
else:
    print("No")