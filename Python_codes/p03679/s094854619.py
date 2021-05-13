X, A, B = map(int, input().split())

print('delicious' if A >= B else ('safe' if (A + X) >= B else 'dangerous'))