n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sum = sum(a)
b_sum = sum(b)

if a_sum > b_sum:
    print("No")
    exit(0)

less_a_cnt = 0
less_b_cnt = 0

for i in range(n):
    if a[i] < b[i]:
        less_a_cnt += int((b[i] - a[i]) / 2)
    else:
        less_b_cnt += a[i] - b[i]

if less_a_cnt < less_b_cnt:
    print("No")
else:
    print("Yes")
