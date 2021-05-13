n, m = map(int, input().split())
a = list(map(int, input().split()))

t = sum(a) / (4*m)
print('Yes' if sum([1 for i in a if i >= t]) >= m else 'No')