import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    m, n, k = map(int, input().split())
    grid = [list(map(int, input())) for _ in range(m)]
    
    # grid が 1 の個数を k 以下にする
    # m <= 10 なので、m についてどこで切るかを全探索 -> その後 n について貪欲
    res = INF
    def adding(j):
        for i in range(m):
            counter[index_to_number[i]] += grid[i][j]

    for U in range(1 << (m - 1)):
        counter = Counter()
        index_to_number = [None] * m
        now = 0
        for i in range(m):
            index_to_number[i] = now
            now += (U >> i) & 1
        score = bin(U).count('1')
        # print(U, index_to_number)
        for j in range(n):
            # 一旦足してみる
            adding(j)
            if max(counter.values()) > k:
                score += 1
                counter.clear()
                adding(j) # もう1回やりなおす
                if max(counter.values()) > k: # やりなおした結果ダメなら無理
                    break
        else: # break されずに済めば OK
            res = min(res, score)

    print(res)
resolve()