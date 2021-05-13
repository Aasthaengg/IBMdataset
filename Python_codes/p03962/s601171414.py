x, y, z = map(int, input().split())
count = 1
if x != y:
    count += 1
if x != z and y != z:
    count += 1
print(count)
