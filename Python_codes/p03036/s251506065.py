r,d,x = map(int,input().split())

def x_pro(x):
    return r*x-d

for i in range(10):
    print(x_pro(x))
    x=x_pro(x)