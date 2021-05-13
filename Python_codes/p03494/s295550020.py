n = int(input())
items = list(map(int, input().split()))
count = 0
while True:
    should_break = False
    for i in range(n):
        if items[i] % 2 == 0:
            items[i] = items[i] / 2
            continue
        else:
            should_break = True
            break
    if should_break:
        break
    count += 1
print(count)