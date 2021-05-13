n = int(input())
a = [int(i) for i in input().split()]

count1 = 0
count2 = 0
sum = 0

for i in range(0,n):
    if i % 2 == 0:
        if sum + a[i] > 0:
            sum += a[i]
            continue
        elif sum + a[i] <= 0:
            count1 += abs(1 - sum -a[i])
            sum = 1
    elif i % 2 == 1:
        if sum + a[i] < 0:
            sum += a[i]
            continue
        else:
            count1 += abs(-1 - sum - a[i])
            sum = -1

sum = 0
for i in range(0,n):
    if i % 2 == 1:
        if sum + a[i] > 0:
            sum += a[i]
            continue
        elif sum + a[i] <= 0:
            count2 += abs(1 - sum -a[i])
            sum = 1
    elif i % 2 == 0:
        if sum + a[i] < 0:
            sum += a[i]
            continue
        else:
            count2 += abs(-1 - sum - a[i])
            sum = -1

if count1 >= count2:
    print(count2)
else:
    print(count1)
