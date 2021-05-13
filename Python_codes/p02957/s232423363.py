A, B = map(int, input().split())
A, B = sorted([A, B])
K = (B + A) / 2
if A <= K <= B and int(K) == K:
    print(int(K))
else:
    print('IMPOSSIBLE')
