n = int(input())
x = list(input().split() for i in range(n))
c = 0

for i in range(n):
    if x[i][1] == 'JPY':
        c += int(x[i][0])
    else:
        y = float(x[i][0]) * 380000.0
        c += y

print(c)