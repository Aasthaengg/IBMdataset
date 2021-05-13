num_list = list(map(int, input().split()))
if (num_list[0] * num_list[1]) % 2 == 1:
    print('Odd')
else:
    print('Even')