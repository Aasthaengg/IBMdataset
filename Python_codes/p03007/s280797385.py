n=int(input())
a=list(map(int,input().split()))
a.sort()
plus,minus=[],[]
for i in range(n):
    if a[i]>=0:
        plus.append(a[i])
    else:
        minus.append(a[i])
order=[]
if plus and minus:
    if len(plus)>=2:
        for num in plus[:-1]:
            order.append((minus[0],num))
            minus[0]-=num
    for num in minus:
        order.append((plus[-1],num))
        plus[-1]-=num
    print(plus[-1])
else:
    if minus:
        a=a[::-1]
    for i in range(1,n-1):
        order.append((a[0],a[i]))
        a[0]-=a[i]
    if minus:
        a=a[::-1]
    order.append((a[-1],a[0]))
    a[-1]-=a[0]
    print(a[-1])
for x,y in order:
    print(x,y)