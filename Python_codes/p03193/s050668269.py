n, h, w = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

count = 0
for i in range(n):
    if a[i] >= h and b[i] >= w:
        count += 1

print(count)