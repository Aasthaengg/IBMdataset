A,B,C=map(int,input().split())
a=(A,B,C)
b=sorted(a)
c=(str(b[2]),str(b[1]))
d=''.join(c)
e=int(d)
print(e+b[0])