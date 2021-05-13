n=int(input())
a=list(map(int,input().split()))
f=0
t=0
z=0
for i in range(n):
    if a[i]%4==0:
        f+=1
    elif a[i]%2==0:
        t+=1
    else:
        z+=1
flg=False
if t==0 and z-1<=f:
    flg=True
if z<=f and t>0:
    flg=True
if flg:
    print("Yes")
else:
    print("No")