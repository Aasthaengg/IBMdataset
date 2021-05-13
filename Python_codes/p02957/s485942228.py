A, B = map(int, input().split())

K = (A+B) / 2
if (A-K) * (B-K) < 0 and K == int(K):
    print(int(K))
else:
    print('IMPOSSIBLE')
