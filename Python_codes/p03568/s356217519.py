from functools import reduce

N = int(input())
A = list(map(int, input().split()))

n = reduce(lambda x, y: x * y, (1 if a % 2 else 2 for a in A))
print(3 ** N - n)
