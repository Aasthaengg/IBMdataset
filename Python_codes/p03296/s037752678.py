n = int(input())
a = list(map(int,input().split()))
p = 0
x = 0
y = 1

for i in range(n):
    if a[i] != x:
        if y == 1:
            x = a[i]
        else:
            p += y // 2
            x = a[i]
            y = 1
    else:
        y += 1

if y == 1:
    print(p)
else:
    print(p + y // 2)