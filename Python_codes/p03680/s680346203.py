n = int(input())
a = [int(input()) for i in range(n)]
b = a[0]
c = 1
d = set()
while b != 2:
    b = a[b - 1]
    if b in d:
        print(-1)
        break
    else:
        d.add(b)
        c += 1
else:
    print(c)