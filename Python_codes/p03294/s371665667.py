from functools import reduce

n = int(input())
a = list(map(int, input().split()))

print(reduce(lambda x, y: x + (y - 1), a, 0))

