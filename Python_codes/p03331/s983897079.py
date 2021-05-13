N = int(input())

minno = 10 ** 5
for i in range(1, N):
    str_list_a = list(str(i))
    int_list_a = [int(x) for x in str_list_a]
    str_list_b = list(str(N - i))
    int_list_b = [int(y) for y in str_list_b]

    sum_a_b = sum(int_list_a) + sum(int_list_b)
    if sum_a_b < minno:
        minno = sum_a_b
print(minno)
