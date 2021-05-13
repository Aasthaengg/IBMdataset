s, c = map(int, input().split())

count = 0

if c / 2 >= s:
    count += s
else:
    count += c // 2

c -= 2 * count

count += c // 4

print(count)
