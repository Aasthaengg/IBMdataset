import itertools
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = []
for i in range(2, N + 1):
    ans.append([1, i])

"""
全ての組み合わせは N_C_2
1を中心にスターグラフを作る
2,3,...,Nの中での組み合わせは N-1_C_2、これらの距離は2
2,3,...,Nの中で、(N-1_C_2 - K) 個の辺を張れば、
距離2の組み合わせがK個残る

N-1_C_2 - K < 0 となる時、構築不可
"""

if (N - 1) * (N - 2) // 2 - K < 0:
    print(-1)
    exit()
else:
    comb = list(itertools.combinations(range(2, N + 1), 2))
    for i in range((N - 1) * (N - 2) // 2 - K):
        u = comb[i][0]
        v = comb[i][1]
        ans.append([u, v])
    print(len(ans))
    for i in ans:
        print(*i)
