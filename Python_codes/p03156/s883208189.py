n = int(input())
a, b = map(int, input().split(' '))
p = list(map(int, input().split(' ')))
x = y = z = 0
for i in range(n):
    if p[i] <= a:
        x += 1
    elif a + 1 <= p[i] <= b:
        y += 1
    else:
        z += 1
print(min([x, y, z]))
