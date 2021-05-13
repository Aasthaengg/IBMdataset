a=[v for v in input().split()]
if a[0]<a[1]:  
    u=int(a[1])
    for i in range (0,u):
        print(a[0],end='')
else:
    u=int(a[0])
    for i in range (0,u):
        print(a[1],end='')