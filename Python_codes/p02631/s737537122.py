from functools import reduce

N = int(input())
A = list(map(int, input().split()))

x = reduce(lambda x, y: x ^ y, A)
print(*[x ^ a for a in A])
