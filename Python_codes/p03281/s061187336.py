number = int(input())

num_eight_divisors = 0

numbers = list(range(9, number + 1, 2))

for i in range(9, number + 1, 2):
    divisors = [1, i]

    for j in range(2, i):
        q, mod = divmod(i, j)

        if mod == 0:
            divisors.append(j)
            divisors.append(q)

    if len(set(divisors)) == 8:
        num_eight_divisors = num_eight_divisors + 1

print(num_eight_divisors)
