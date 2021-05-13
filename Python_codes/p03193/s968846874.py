n, h, w = map(int, input().strip().split(' '))
count = 0
for i in range(n):
    a, b = map(int, input().strip().split(' '))
    if a>= h and b>= w:
        count += 1

print(count)