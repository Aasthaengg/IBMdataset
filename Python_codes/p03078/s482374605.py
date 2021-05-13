import heapq
from collections import defaultdict

# 3種類のケーキを美味しい順にソートする
x, y, z, k = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)


# heapqで管理
que = []
heapq.heapify(que)
# 最も美味しい組み合わせは、
heapq.heappush(que, ((A[0] + B[0] + C[0])*-1, (0, 0, 0)))

# 使用した組み合わせ
used = defaultdict(int)
used[(0, 0, 0)] = 1

ans = []
while len(ans) < k:
    total, comb = heapq.heappop(que)
    ans.append(total*-1)
    a, b, c = comb
    # その次に美味しい組み合わせは、以下のいずれか
    for p, q, r in [[a+1, b, c], [a, b+1, c], [a, b, c+1]]:
        if used[(p, q, r)] == 0 and p < x and q < y and r < z:
            heapq.heappush(que, ((A[p] + B[q] + C[r])*-1, (p, q, r)))
            used[(p, q, r)] = 1

for i in range(k):
    print(ans[i])