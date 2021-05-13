r,D,X=map(int,input().split())

a=X

for i in range(10):
    a=r*a-D
    print(a)