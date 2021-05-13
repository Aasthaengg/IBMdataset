n = int(input())
a = list(map(int, input().split()))
count_1 = 0
count_2 = 0
sum_1 = 0
sum_2 = 0

for i in range(len(a)):
    sum_1 += a[i]
    if i % 2 == 1:
        if sum_1 <= 0:
            count_1 += 1 - sum_1
            sum_1 = 1
    elif i % 2 == 0:
        if sum_1 >= 0:
            count_1 += sum_1 + 1
            sum_1 = -1

for i in range(len(a)):
    sum_2 += a[i]
    if i % 2 == 1:
        if sum_2 >= 0:
            count_2 += sum_2 + 1
            sum_2 = -1
    elif i % 2 == 0:
        if sum_2 <= 0:
            count_2 += 1 - sum_2
            sum_2 = 1

print(count_1 if count_1 < count_2 else count_2)