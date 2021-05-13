a, b, c = map(lambda x: int(x), input().split(' '))
print('YES') if a - b == b - c  else print('NO')
