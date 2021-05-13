import collections

S = input()

N = 3
L = (list(collections.Counter(S).values()) + [0] * N)[:N]
min_L = min(L)
L = map(lambda l: l - min_L <= 1, L) # 差が1以下か
print('YES' if all(L) else 'NO')