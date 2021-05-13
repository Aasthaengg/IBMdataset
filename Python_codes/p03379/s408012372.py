n = int(input())
x = [int(i) for i in input().split()]
y = sorted(x)
a , b = y[n//2-1], y[n//2]
for i in x:
    if i > a:
        print(a)
    else:
        print(b)