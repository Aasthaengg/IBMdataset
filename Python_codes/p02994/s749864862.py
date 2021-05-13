n,l=map(int,input().split())
a=10*10
b=int(n*(n+2*l-1)/2)
for i in range(1,n+1):
    if abs(b-a)>abs(l+i-1):
        a=(b-l-i+1)
print(a)