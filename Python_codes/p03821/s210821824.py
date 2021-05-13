n = int(input())
a,b=[],[]

for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

a=list(reversed(a))
b=list(reversed(b))

ans=0
OK=0
for i in range(n):
    tmp=a[i]+OK
    if tmp<=b[i] and tmp!=0:
        ok=b[i]-tmp
    elif tmp==0:
        continue
    else:
        ok=-(-tmp//b[i])*b[i]-tmp
    OK=OK+ok

print(OK)