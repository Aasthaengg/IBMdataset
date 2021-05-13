n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
D1=0
for i in range(n):
    D1+=abs(x[i]-y[i])
D2=0
for i in range(n):
    D2+=(x[i]-y[i])**2
D2=D2**0.5
D3=0
for i in range(n):
    D3+=abs(x[i]-y[i])**3
D3=D3**(1/3)
D4=0
for i in range(n):
    if D4<=abs(x[i]-y[i]):
        D4=abs(x[i]-y[i])
print("%.6f\n%.6f\n%.6f\n%.6f\n" %(D1,D2,D3,D4))