h, n = map(int, input().split())
a = map(int, input().split())
print('Yes' if h <= sum(a) else 'No')