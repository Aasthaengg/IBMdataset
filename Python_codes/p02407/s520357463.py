n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

b = []
for i in range(n):
    b.append(a[n - 1 - i])

for i in range(n):
    if i < n - 1:
        print(b[i], end=' ')
    else:
        print(b[i])
