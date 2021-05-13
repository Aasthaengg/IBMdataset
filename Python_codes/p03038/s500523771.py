from collections import defaultdict

N, M = map(int, input().split())
# Aは昇順に並べる
A = list(sorted(map(int, input().split())))

# B,Cの対応辞書を作り、C順に並べる
counter = defaultdict(int)
for _ in range(M):
    B, C = map(int, input().split())
    counter[C] += B
c_list = list(sorted(counter.keys(), reverse=True))

# Cを大きい順に個数分並べたリストを作る
moves = []
n = 0
for c in c_list:
    b = counter[c]
    if n + b < N:
        p = b
    else:
        p = N - n
    for i in range(p):
        moves.append(c)
    if len(moves) >= N:
        break

# AとCを小さい順に比較
siz = min(N, len(moves))
for i in range(siz):
    # Aの小さいものを上書き
    A[i] = max(A[i], moves[i])

print(sum(A))
