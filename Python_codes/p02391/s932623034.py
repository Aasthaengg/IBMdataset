(a, b) = map(int, input().split())
print('a', end=' ')
print('<' if a < b else '==' if a==b else '>', end=' ')
print('b')