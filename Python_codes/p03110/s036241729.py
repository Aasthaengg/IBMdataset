n=int(input())
x=[]
u=[]
for i in range(n):
    X,U=input().split()
    x.append(float(X))
    u.append(U)
    X=""
    U=""
#print(x)
#print(u)
sum=0
for i in range(n):
    if u[i]=="JPY":
        sum+=x[i]
    elif u[i]=="BTC":
        sum+=x[i]*380000.0
print(sum)