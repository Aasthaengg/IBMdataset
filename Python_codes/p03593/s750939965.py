import collections
h,w=map(int,input().split())
a=''
for i in range(h):
    a+=str(input())
l=list(a)
r=collections.Counter(l)
rr=list(r.values())
R=[]
x=0;y=0;z=0
for i in rr:
    R.append(i%4)
    if i%4==1 or i%4==3:
        x+=1
    elif i%4==2:
        y+=1
    else:
        z+=1

if h%2==0 and w%2==0:
    if x==0 and y==0:
        print('Yes')
    else:
        print('No')
elif h%2==1 and w%2==1:
        if x<=1 and y<=(h-1)//2+(w-1)//2:
            print('Yes')
        else:
            print('No')
else:
    if h%2==0:
        if x==0 and y<=h//2:
            print('Yes')
        else:
            print('No')
    else:
        if x==0 and y<=w//2:
            print('Yes')
        else:
            print('No')
