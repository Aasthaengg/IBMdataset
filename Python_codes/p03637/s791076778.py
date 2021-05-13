input()

numbers = tuple(map(int, input().split(' ')))

n_4_multiples = 0
n_2_multiples = 0
n_other = 0

for n in numbers:
    if n % 4 == 0:
        n_4_multiples += 1
    elif n % 2 == 0:
        n_2_multiples += 1
    else:
        n_other += 1

if n_2_multiples > 0:
    n_other += 1

if n_other - n_4_multiples <= 1:
    print('Yes')
else:
    print('No')
