# ABC119B

n = int(input())

z = 0
for i in range(n):
    x, y = input().split()
    x = float(x)
    if y == 'JPY':
        z += x
    else:
        z += x*380000
print(z)
