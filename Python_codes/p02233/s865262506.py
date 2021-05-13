n=int(input())
a=1
b=1
if n==0 or n==1:
    print(1)
else:
    for i in range (n):
        a,b=b,a+b
    print(a)
