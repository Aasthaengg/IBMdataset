a, b, c = sorted(map(int, input().split()))
print('Yes' if a < c and (a == b or b == c) else 'No')
