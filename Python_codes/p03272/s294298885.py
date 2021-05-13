n, i = map(int, input().split())

count = 0

for num in range(n, 0, -1):
    count += 1
    if num == i:
        break
print(count)