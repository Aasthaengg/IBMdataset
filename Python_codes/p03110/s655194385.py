n=int(input())
y=[]
t=[]
l=[]
for i in range(n):
    x,u=input().split()
    y.append(float(x))
    t.append(u)
for i in range(n):
    if t[i]=='JPY':
        l.append(y[i])
    else:
        l.append(y[i]*380000.0)
print(sum(l))