r,D,x=map(int,input().split())
x_pre=x
for i in range(10):
    X=r*x_pre-D
    x_pre=X
    print(X)