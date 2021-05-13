na = 0
a = []
b = []
n = int(input())

for i in range(n):
    a.append(int(input()))

for i in range(n):
    b.append(a[na])
    if a[na] == 2:
        print(i + 1)
        break
    na = a[na] - 1
else:
    print(-1)