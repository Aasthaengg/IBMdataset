n, h, w = map(int, input().split())

count = 0
for i in range(n):
    a, b = map(int, input().split())
    if h <= a and w <= b:
        count = count + 1

print(count)