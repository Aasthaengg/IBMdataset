K, X = map(int, input().split(' '))

print(' '.join([str(n) for n in range(max(-1000000, X - K + 1), min(1000001, X + K))]))
