N = int(input())

min_sum = 100000

for A in range(1, N):
    Sum = 0
    sum_A = 0
    sum_B = 0
    B = N - A
    str_A = str(A)
    str_B = str(B)
    for i in str_A:
        sum_A += int(i)
    for j in str_B:
        sum_B += int(j)
    Sum = sum_A + sum_B
    if Sum < min_sum:
        min_sum = Sum
    
print("{}".format(min_sum))