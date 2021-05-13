n = int(input())
a = list(input().split())

r = 0
c = 1
h = a[0]
for i in range(1, n):
    if h == a[i]:
        c += 1
        if c%2==0:
            r += 1
    else:
        c = 1
        h = a[i]
print(r)