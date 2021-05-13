a=[]
b=[]
op=[]
while True:
    x,y,z=raw_input().split()
    if(y=='?'):
        break
    a.append(int(x))
    op.append(y)
    b.append(int(z))
A=iter(a)
B=iter(b)
OP=iter(op)
for n in A:
    p=B.next()
    q=OP.next()

    if(q=='+'):
        print(n+p)
    elif(q=='*'):
        print(n*p)
    elif(q=='-'):
        print(n-p)
    elif(q=='/'):
        print(n/p)