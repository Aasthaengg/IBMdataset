n = int(input())

max_1 = 0
max_2 = 0
max_index = 0

for i in range(n):
    item = int(input())
    if item >= max_1:
        max_1, max_2 = item, max_1
        max_index = i
    elif item > max_2:
        max_2 = item

for i in range(n):
    ans = max_2 if i == max_index else max_1
    print(ans)

