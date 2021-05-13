n = int(input())
a = list(int(input()) for i in range(n))
b = sorted(list(a))
x = b[-1]
y = b[-2]
for i in range(n):
    if a[i] != x:
        print(x)
    else:
        print(y)