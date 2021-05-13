n=int(input())
l,d=[],[]
for i in range(n):
    x=int(input())
    if(x%10==0):
        l.append(x)
    else:
        d.append(x)
if(d==[]):
    print(0)
else:
    s=sum(l)+sum(d)
    if(s%10==0):
        print(s-min(d))
    else:
        print(s)
