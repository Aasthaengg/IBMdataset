num_int = int(input())
sum_of_rest_num = 0
for i in range(1, num_int + 1):
    if not (i % 15 == 0 or i % 3 == 0 or i % 5 == 0):
        sum_of_rest_num += i

print(sum_of_rest_num)