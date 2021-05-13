r,D,x2000=map(int,input().split())
a=[]
for i in range(10):
    x2000=r*x2000-D
    a.append(x2000)
    print(x2000)