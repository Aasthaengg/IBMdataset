a, b, c, d = map(int, input().split())
print('Yes') if (abs(a - c) <= d) | ((abs(a - b) <= d) & (abs(c - b) <= d)) else print('No')
