n,m,c=map(int,input().split())
b=[int(_) for _ in input().split()]
l=[]
for i in range(n):
    a=[int(_) for _ in input().split()]
    x=c
    for j in range(m):
        x+=a[j]*b[j]
    if x>0:
        l.append(x)
print(len(l))