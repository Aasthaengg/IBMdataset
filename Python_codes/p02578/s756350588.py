n = int(input())
total = 0
a = [int(v) for v in input().split()]
highest = a[0]
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]
    if second < first:
        diff = first - second
        a[i] = second + diff
        total += diff
print(total)