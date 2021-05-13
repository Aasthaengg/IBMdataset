n = int(input())
a = list(map(int, input().split()))

sum_water = sum(a) // 2

sum_even_left = [0]
sum_odd_left = [0]
for i in range(n):
    if i % 2 == 0:
        sum_even_left.append(sum_even_left[-1] + a[i])
    else:
        sum_odd_left.append(sum_odd_left[-1] + a[i])

sum_even_right = [0]
sum_odd_right = [0]
for i in range(n-1, -1, -1):
    if i % 2  == 0:
        sum_even_right.append(sum_even_right[-1] + a[i])
    else:
        sum_odd_right.append(sum_odd_right[-1] + a[i])
sum_even_right = sum_even_right[::-1]
sum_odd_right = sum_odd_right[::-1]

for i in range(n):
    if i % 2 == 0:
        print(2 * (sum_water - sum_even_left[i//2] - sum_odd_right[i//2]), end=' ')
    else:
        print(2 * (sum_water - sum_odd_left[i//2] - sum_even_right[i//2+1]), end=' ')