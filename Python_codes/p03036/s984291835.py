r,d,x_2000=map(int,input().split())
x=[x_2000]
for i in range(10):
    temp=r*x[i]-d
    x.append(temp)
    print(temp)