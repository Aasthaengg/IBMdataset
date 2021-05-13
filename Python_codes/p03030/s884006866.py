n = int(input())
a = []
for i in range(n):
    a.append(list(input().split()))
b = a
for i in range(n):
    b[i][1] = -int(b[i][1])
b = sorted(b)
for i in range(n):
    b[i][1] = -b[i][1]
    print(a.index(b[i])+1)