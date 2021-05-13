n=int(input())
t=[0]*n
a=[0]*n
for i in range(n):
    t[i],a[i]=map(int,input().split())
curt=t[0]
cura=a[0]
for i in range(1,n):
    if t[i]>=curt and a[i]>=cura:
        curt=t[i]
        cura=a[i]
    else:
        kt=curt//t[i]
        if curt%t[i]:
            kt+=1
        ka=cura//a[i]
        if cura%a[i]:
            ka+=1

        k=max(kt,ka)
        curt=t[i]*k
        cura=a[i]*k
print(curt+cura)

