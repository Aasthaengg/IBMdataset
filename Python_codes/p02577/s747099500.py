from functools import reduce
print('Yes') if reduce(lambda x, y: x + y, map(int, list(input()))) % 9 == 0 else print('No')