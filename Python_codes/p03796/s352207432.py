from functools import reduce

N = int(input())
div = pow(10, 9) + 7
print(reduce(lambda ans, n: ans * n % div, range(1, N + 1)))