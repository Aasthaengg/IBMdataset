n = int(input())
a = [int(s) for s in input().split()]

sum1 = 0
count = 0
total_length = sum(a)

for i in range(len(a)):
    sum1 += a[i]
    if sum1 >= total_length / 2:
        count1 = abs(sum1 - sum(a[i + 1:]))
        count2 = abs(sum1 - a[i] - sum(a[i:]))
        if count1 <= count2:
            count = count1
        else:
            count = count2
        break
print(count)
