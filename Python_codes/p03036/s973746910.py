r,D,x = map(int,input().split())
l = [x]
for i in range(10):
    x = r*x - D
    print(x)