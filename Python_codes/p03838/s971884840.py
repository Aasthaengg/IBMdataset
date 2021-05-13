x, y = map(int, input().split())

count1 = abs(y + x) + 1
count2 = max(y - x, x - y + 2)

print(min(count1, count2))