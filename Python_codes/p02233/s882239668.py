n=int(input())
x=1
y=1
a=0
for i in range(n):
    a=x
    x=y
    y=a+y
print(x)
