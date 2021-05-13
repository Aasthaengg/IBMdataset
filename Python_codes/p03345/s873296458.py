def f(a,b,c):
    return b+c,a+c,a+b
a,b,c,k = map(int,input().split())
if k%2 ==0:
    print(a-b)
else:
    print(b-a)



