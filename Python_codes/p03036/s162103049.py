a = input().split()
r = int(a[0])
D = int(a[1])
x = int(a[2])
for i in range(10):
    if i == 0:
        xx = r * x - D
    else:
        xx = r * xx -D
    print(xx)
