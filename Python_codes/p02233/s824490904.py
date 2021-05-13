n=int(input())
a=b=1
for i in range(n):
    a,b=b,a+b
    n-=1
print(a)

