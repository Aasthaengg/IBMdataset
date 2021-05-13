number_str = input()
number_int = int(number_str)

n_100 = number_int // 100
n_10 = number_int // 10 *10
n_1 = number_int - n_10

if n_100 == n_1:
    print('Yes')
else:
    print('No')