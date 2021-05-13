k, x = map(int, input().split())
s = x - k + 1
e = x + k - 1
l = list(range(s, e+1))
print(' '.join(map(str, l)))