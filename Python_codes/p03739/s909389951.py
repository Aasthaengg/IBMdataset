import copy

n = int(input())
a = list(map(int, input().split(' ')))
sum_list = [0] * n
past = 0
for i in range(n):
    if i > 0:
        sum_list[i] = sum_list[i-1] + a[i]
    else:
        sum_list[0] = a[i]
sum1 = copy.copy(sum_list)
sum2 = copy.copy(sum_list)

ans = 0
count = 0
for i in range(n):
    # a[0]がプラス
    num = 0
    sum1[i] += past
    if i % 2 == 0 and sum1[i] <= 0:
        num = (abs(sum1[i]) + 1)
        sum1[i] += num
        past += num
    if i % 2 == 1 and sum1[i] >= 0:
        num = (abs(sum1[i]) + 1)
        sum1[i] -= num
        past -= num
    count += num

ans = count
count = 0
past = 0

for i in range(n):
    # a[0]がマイナス
    num = 0
    sum2[i] += past
    if i % 2 == 0 and sum2[i] >= 0:
        num = (abs(sum2[i]) + 1)
        sum2[i] -= num
        past -= num
    if i % 2 == 1 and sum2[i] <= 0:
        num = (abs(sum2[i]) + 1)
        sum2[i] += num
        past += num
    count += num

ans = min(ans, count)
print(ans)