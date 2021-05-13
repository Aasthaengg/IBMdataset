n = int(input())
d, x = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

k = []
for i in range(n):
    count = 0
    day = d
    while True:
        day -= (count * a[i]) + 1
        if day >= 0:
            count += 1
            day = d
        else:
            k.append(count)
            break
total = sum(k) + x
print(total)