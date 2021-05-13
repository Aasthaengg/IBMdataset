N = int(input())
v = list(map(int, input().split()))

first = {}
second = {}

for x in range(N):
    if x % 2 == 0:
        first.setdefault(v[x], 0)
        first[v[x]] += 1
    else:
        second.setdefault(v[x], 0)
        second[v[x]] += 1

first_sorted = sorted(first.items(), key=lambda x: x[1], reverse=True)
second_sorted = sorted(second.items(), key=lambda x: x[1], reverse=True)
sum_change_1 = 0

first_value = 0
for y in range(len(first_sorted)):
    if y == 0:
        first_value = first_sorted[y][0]
    if y != 0:
        sum_change_1 += first_sorted[y][1]

for z in range(len(second_sorted)):
    if first_value != second_sorted[0][0]:
        if z != 0:
            sum_change_1 += second_sorted[z][1]
    else:
        if z != 1:
            sum_change_1 += second_sorted[z][1]

sum_change_2 = 0

first_value = 0
for v in range(len(second_sorted)):
    if v == 0:
        first_value = second_sorted[v][0]
    if v != 0:
        sum_change_2 += second_sorted[v][1]

for w in range(len(first_sorted)):
    if first_value != first_sorted[0][0]:
        if w != 0:
            sum_change_2 += first_sorted[w][1]
    else:
        if w != 1:
            sum_change_2 += first_sorted[w][1]

print(min(sum_change_1, sum_change_2))
