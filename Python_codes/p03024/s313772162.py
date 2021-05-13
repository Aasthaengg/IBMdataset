S = input()
N = len(S)

nokori = 15 - N
nece = 8 - nokori  # 現時点で必要な勝利数

if S.count('o') >= nece:
    print('YES')
else:
    print('NO')
