N = input()

sumRes = sum(list(map(int, N)))

print('Yes' if sumRes % 9 == 0 else 'No')
