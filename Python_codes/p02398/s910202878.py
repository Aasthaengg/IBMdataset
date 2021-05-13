a, b, c = map(int, input().split())
x = a
count = 0
for _ in range(b - a + 1):
    if c % x == 0:
        count += 1
    x += 1
print(count)
