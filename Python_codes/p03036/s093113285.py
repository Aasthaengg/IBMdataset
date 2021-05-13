r,d,X=map(int,input().split())
x=[X]
for i in range(10):
    x.append(r*x[i]-d)
del x[0]
#print(x)
for i in range(len(x)):
    print(x[i])