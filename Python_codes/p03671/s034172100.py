#ABC066A
a,b,c = map(int,input().split())
if (a == b)&(b == c):
    print(a + b)
elif(a > b)&(a > c):
    print(b + c)
elif (b > a)&(b > c):
    print(a + c)
elif (c > a)&(c > b):
    print(a + b)