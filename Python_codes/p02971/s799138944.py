n = int(input())
a = [int(input()) for i in range(n)]
b = tuple(a)
a.sort()
for i in b:
    if i == a[n-1]:
        print(a[n-2])
    else:
        print(a[n-1])