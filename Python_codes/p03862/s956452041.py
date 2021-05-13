N,x=list(map(int,input().split()))
a=list(map(int,input().split()))

op=0

for i in range(N-1):
    s=a[i]+a[i+1]
    opc=max(0,s-x)
    a[i+1]=max(0,a[i+1]-opc)
    op+=opc

print(op)