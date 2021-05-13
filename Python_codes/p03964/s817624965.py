n = int(input())
a,b = 1,1
for _ in range(n):
    x,y = map(int,input().split())
    k = -min(-a//x,-b//y)
    a,b = k*x,k*y
print(a+b)