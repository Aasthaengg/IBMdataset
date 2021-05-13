n=int(input())
x0=int(input())
ma=-1111111111
mi=x0
for _ in range(n-1):
    x=int(input())
    if ma<x-mi:
        ma=x-mi
    if mi>x:
        mi=x
print(ma)