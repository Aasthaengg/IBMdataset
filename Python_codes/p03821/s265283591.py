n = int(input())
a,b=[],[]

for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

a=list(reversed(a))
b=list(reversed(b))

OK=0
for i in range(n):
    A=a[i]+OK
    if A<b[i]:
        ok=b[i]-A
    if A==b[i]:
        continue
    else:
        ok=-(-A//b[i])*b[i]-A
    OK+=ok

print(OK)
