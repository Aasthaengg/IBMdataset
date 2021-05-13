n = int(input())
a = list(map(int, input().split()))
a.append(0)

x = 1000
y = 0

for i in range(n):
    if a[i] < a[i+1]:
        y += x // a[i]
        x %= a[i]
    elif a[i] > a[i+1]:
        x += y * a[i]
        y = 0

print(x)
