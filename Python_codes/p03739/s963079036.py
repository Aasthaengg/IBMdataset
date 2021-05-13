n = int(input())
A = [int(i) for i in input().split()]

seq_sum = 0
sign = 1
count_1 = 0
for i in range(n):
    if A[i] * sign * (-1) > seq_sum * sign:
        seq_sum += A[i]
    else:
        count_1 += abs(sign * (-1) - (seq_sum + A[i]))
        seq_sum += A[i] + (sign * (-1) - (seq_sum + A[i]))
    sign = sign * (-1)

seq_sum = 0
sign = -1
count_2 = 0
for i in range(n):
    if A[i] * sign * (-1) > seq_sum * sign:
        seq_sum += A[i]
    else:
        count_2 += abs(sign * (-1) - (seq_sum + A[i]))
        seq_sum += A[i] + (sign * (-1) - (seq_sum + A[i]))
    sign = sign * (-1)

print(min(count_1, count_2))