input()
a, *b = sorted(map(int, input().split()), reverse=True)
print('Yes' if a < sum(b) else 'No')