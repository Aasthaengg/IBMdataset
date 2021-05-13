# import itertools
# import math
# import sys
# sys.setrecursionlimit(500*500)
# import numpy as np

# N = int(input())
S = input()
# n, *a = map(int, open(0))
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# tree = [[] for _ in range(N + 1)]
# B_C = [list(map(int,input().split())) for _ in range(M)]
# S = input()

# B_C = sorted(B_C, reverse=True, key=lambda x:x[1])
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement(range(1, M + 1), N))
# itertools.product((0,1), repeat=n)

# A = np.array(A)
# cum_A = np.cumsum(A)
# cum_A = np.insert(cum_A, 0, 0)

# def dfs(tree, s):
#     for l in tree[s]:
#         if depth[l[0]] == -1:
#             depth[l[0]] = depth[s] + l[1]
#             dfs(tree, l[0])
# dfs(tree, 1)

Q = int(input())
query = [list(input().split()) for _ in range(Q)]
direction = 1
S_front = ""
S_back = ""
for l in query:
    if l[0] == "1":
        direction *= -1
    else:
        if (l[1] == "1" and direction == 1) or (l[1] == "2" and direction == -1):
            S_front += l[2]
        else:
            S_back += l[2]

if direction == 1:
    print(S_front[::-1] + S + S_back)
else:
    print(S_back[::-1] + S[::-1] + S_front)