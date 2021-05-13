a = [int(s) for s in input().split()]
max_id = a.index(max(a[0], a[1], a[2]))
min_id = a.index(min(a[0], a[1], a[2]))
sum = 0
sum += abs(a[0] - a[1])
sum += abs(a[1] - a[2])
sum += abs(a[2] - a[0])
sum -= abs(a[max_id] - a[min_id])
print(sum)