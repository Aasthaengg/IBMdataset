d, n = map(int, input().split())
x = 100 **d
if n != 100:
    print(x*n)
else:
    print(x*(n +1))