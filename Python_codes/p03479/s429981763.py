x, y = map(int, input().split())

z = x * 2
count = 1
while z <= y:
    count += 1
    z = z * 2

print(count)