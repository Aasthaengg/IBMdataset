s = ''.join(sorted(input()))
t = ''.join(reversed(sorted(input())))

print('Yes' if s < t else 'No')