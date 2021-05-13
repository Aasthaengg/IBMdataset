A, B, K = map(int, input().split())
count = 0
if K == 0:
    print('%d %d' % (A, B))
elif K <= A:
    print('%d %d' % (A-K, B))
elif A < K <= B+A:
    print('%d %d' % (0, B-(K-A)))
else:
    print('0 0')
