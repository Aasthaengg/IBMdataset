n,x=map(int,input().split())
*a,=map(int,input().split())
b=[]
b.append(min(a[0],x))
for i in range(1,n):
    b.append(max(min(x-b[i-1], a[i]),0))

print(sum(a)-sum(b))