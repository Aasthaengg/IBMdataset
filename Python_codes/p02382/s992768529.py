n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

A=0
B=0
C=0
z=[]
for i in range(n):
    A+=abs(x[i]-y[i])
    B+=(x[i]-y[i])*(x[i]-y[i])
    C+=(abs(x[i]-y[i]))**3
    z.append(abs(x[i]-y[i]))
D=max(z)

    
B=B**(1/2)
C=C**(1/3)

print(A)
print(B)
print(C)
print(D)

