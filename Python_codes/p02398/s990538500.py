(a, b, c) = tuple([int(i) for i in input().split(' ')])
num_divisor = 0
for i in range(a, b + 1):
    if ((c % i) == 0):
        num_divisor += 1

print(num_divisor)