n = int(input())
a = list(map(int, input().split()))
a.sort()
x, y = a[0], a[-1]
w, z = a[0], a[-1]
for i in a[1:-1]:
    if i < 0:
        y -= i
    else:
        x -= i
print(y - x)
for i in a[1:-1]:
    if i < 0:
        print(z, i)
        z -= i
    else:
        print(w, i)
        w -= i
print(z, w)