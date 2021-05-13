n=int(input())
a=list(map(int,input().split()))
b=[0]*n
x=-1
y=2*10**9
z=(x+y)//2
for i in range(1000):
    b[0]=z
    for j in range(1,n):
        b[j]=a[j-1]*2-b[j-1]
    if b[0]+b[-1]>2*a[-1]:
        y=z
        z=(x+y)//2
    elif b[0]+b[-1]<2*a[-1]:
        x=z
        z=(x+y)//2
    else:
        break
    if z%2==1:
        y+=1
        z+=1
print(*b)