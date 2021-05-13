n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sum(a) / (4 * m)
print('Yes' if b <= sorted(a)[-m] else 'No')