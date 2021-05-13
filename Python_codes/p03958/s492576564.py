k, t = map(int, input().split())

A = list(map(int, input().split()))

A = list(reversed(sorted(A)))

left_sum = 0
right_sum = 0
for i in A:
    if left_sum < right_sum :
        left_sum += i
    else:
        right_sum += i

if abs(left_sum - right_sum) in [0, 1]:
    print(0)
else:
    a = abs(left_sum - right_sum) - 1
    print(a)