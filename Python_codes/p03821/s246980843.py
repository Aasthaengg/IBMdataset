n = int(input())
a = []
b = []
for j in range(n):
    l = list(map(int, input().split()))
    a.append(l[0])
    b.append(l[1])
c = 0
for i in range(n-1, -1, -1):
    if (a[i]+c) % b[i] != 0:
        c += (b[i] - (a[i]+c) % b[i])
print(c)