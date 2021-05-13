a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
x = []
y = []
z = []

for i in range(a[0]):
    b = input().split()
    for j in range(a[1]):
        b[j] = int(b[j])
    x.append(b)
    z.append(0)
for i in range(a[1]):
    c = int(input())
    y.append(c)  
for i in range(a[0]):
    for j in range(a[1]):
        z[i] += x[i][j]*y[j]
for i in z:
    print(i)
