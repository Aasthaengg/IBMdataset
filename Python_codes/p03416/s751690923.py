a, b = map(int, input().split())

count = 0
for i in range(a, b + 1):
    l = list(str(i))
    up = l[:(len(l) // 2)]
    if len(l) % 2 == 0:
        down = l[len(l) // 2:]
        down.reverse()
    else:
        down = l[(len(l) // 2) + 1:]
        down.reverse()
    if up == down:
        count += 1

print(count)