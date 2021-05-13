a,b,c,d=map(int, input().split())

x1 = a/2
y1 = b/2

if x1 == c and y1 == d:
    print(a*b/2,1)
else:
    print(a*b/2,0)