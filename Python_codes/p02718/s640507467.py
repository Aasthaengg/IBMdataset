n, m = map(int, input().split())
a = [int(x) for x in input().split()]
total = sum(a)
count = sum(1 for x in a if x >= total / (4*m))
print('Yes' if count >= m else 'No')
