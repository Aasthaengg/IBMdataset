A, B, K = list(map(int, input().split(' ')))
v = max(0, A - K)
w = max(0, B - max(0, (K - A)))
print('{} {}'.format(v, w))