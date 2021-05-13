import sys
from collections import deque

sys.setrecursionlimit(10000)
INF = float('inf')

assert 2 ** 18 == 262144

# def cumxor(li):
#     return list(itertools.accumulate(li, operator.xor))
#
#
# def xors(li):
#     """
#     :param list of int li:
#     :return:
#     """
#     cumxors = cumxor(li)
#     n = len(li) // 2
#     xors = []
#     for i in range(n):
#         st = li.index(i)
#         en = li.index(i, st + 1)
#         xors.append(cumxors[en - 1] ^ cumxors[st])
#     return xors


M, K = list(map(int, input().split()))

if K == 0:
    ans = []
    for i in range(2 ** M):
        ans.append(i)
        ans.append(i)
    print(*ans)
    exit()

if M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    exit()

if K >= 2 ** M:
    print(-1)
    exit()

ans = deque()
ans.append(K)
for i in range(2 ** M):
    if i == K:
        continue
    ans.append(i)
    ans.appendleft(i)
ans.append(K)
print(*ans)
