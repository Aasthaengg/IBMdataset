k=int(input())
l=[i for i in range(1,10)]
for i in range(k):
    r=l.pop(0)
    rr=r%10
    if rr!=0:
        l.append(10*r+rr-1)
    l.append(10*r+rr)
    if rr!=9:
        l.append(10*r+rr+1)
print(r)