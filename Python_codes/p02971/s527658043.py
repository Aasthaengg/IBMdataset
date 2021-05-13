
n = int(input())
a = [int(input()) for _ in range(n)]

if n == 2:
    print(a[1])
    print(a[0])
    exit()

b = [0] * n
for i in range(n):
    b[i] = a[i]

b.sort()
b.reverse()

for i in range(n):
    if a[i] == b[0]:
        print(b[1])
    else:
        print(b[0])


