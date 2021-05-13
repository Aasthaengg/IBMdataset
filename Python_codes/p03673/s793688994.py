
n = int(input())
a = list(map(int,input().split()))
a = [0] + a

dam1=[]
dam2=[]
for i in range(1,n+1):
    if i%2==1:
        dam1.append(a[i])
    else:
        dam2.append(a[i])

if n%2==0:
    dam2.reverse()
    out=dam2 + dam1
elif n%2==1:
    dam1.reverse()
    out=dam1 + dam2
print(*out)
