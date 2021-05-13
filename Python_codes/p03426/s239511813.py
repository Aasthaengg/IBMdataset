import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from collections import defaultdict

H, W, D = map(int, input().split())
A = [list(map(int, input().split()))  for _ in range(H)]

dic = defaultdict(list)

for h in range(H):
    for w in range(W):
        dic[A[h][w]] = [h, w]

def calc(l, r):
    return abs(dic[l][0] - dic[r][0]) + abs(dic[l][1] - dic[r][1])

lst = [0] * (H * W + 1)
for d in range(1, D + 1):
    tmp = d
    while tmp + D <= (H * W):
        lst[tmp + D] = lst[tmp] + calc(tmp, tmp + D)
        tmp += D

# print (lst)
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    ans = lst[R] - lst[L]
    print (ans)
