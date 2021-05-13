n=int(input())
a=sorted(list(map(int,input().split())))
c=1
x=[]
for i in range(n-1):
    if a[i]!=a[i+1]:
        if c>=2:
            x.append(a[i])
        if c>=4:
            x.append(a[i])
        c=1
    else:
        c+=1
if c>=2:
    x.append(a[n-1])
if c>=4:
    x.append(a[n-1])
if len(x)<=1:
    print(0)
else:
    print(x[-1]*x[-2])
