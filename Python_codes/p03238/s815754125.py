from functools import reduce

print(reduce(lambda x, y: x + y, [int(input()) for i in range(2)])) if input() == '2' else print('Hello World')