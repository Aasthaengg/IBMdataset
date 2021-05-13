#ARC73-C
n,T=map(int,input().split())
t=list(map(int,input().split()))
e=T
total=T
for i in range(1,n):
    if t[i]<e:
        total=total-(e-t[i])+T
        e=t[i]+T
    else:
        e=t[i]+T
        total+=T
print(total)