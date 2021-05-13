n = int(input())
a = list(map(int,input().rstrip().split(" ")))
summ = 0
ans_when_odd_indexes_plus = 0
ans_when_odd_indexes_minus = 0
for i in range(n):
    summ += a[i]
    if i % 2 == 0:
        if summ <= 0:
            ans_when_odd_indexes_plus += 1 - summ
            summ = 1
    else:
        if summ >= 0:
            ans_when_odd_indexes_plus += 1 + summ
            summ = -1

summ = 0
for i in range(n):
    summ += a[i]
    if i % 2 == 1:
        if summ <= 0:
            ans_when_odd_indexes_minus += 1 - summ
            summ = 1
    else:
        if summ >= 0:
            ans_when_odd_indexes_minus += 1 + summ
            summ = -1

print(min(ans_when_odd_indexes_plus,ans_when_odd_indexes_minus))