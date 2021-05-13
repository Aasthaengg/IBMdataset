import itertools

N = int(input())
st = set(x * y for x, y in itertools.product(range(1, 10), repeat=2))
print('Yes' if N in st else 'No')
