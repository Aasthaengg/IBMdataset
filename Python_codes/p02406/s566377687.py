n = int(input())
print(' ' + ' '.join(str(x) for x in range(1, n+1) if not x%3 or '3' in str(x)))