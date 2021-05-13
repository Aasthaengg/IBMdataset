import sys
sys.setrecursionlimit(10 ** 6)


def dfs(s, pos):
    global N, K
    ns = {}
    if len(A) > K:
        return
    for i in pos:
        ni = i + 1
        if ni < N:
            x = s + S[ni]
            if x in ns:
                ns[x].append(ni)
            else:
                ns[x] = [ni]
    candidate = []
    for x in list(ns.keys()):
        candidate.append((x, ns[x]))
    candidate.sort()
    for c, idx in candidate:
        A.add(c)
        dfs(c, idx)


S = list(input())
N = len(S)
K = int(input())
alpha = [chr(ord('a') + i) for i in range(26)]

A = set()
for c in alpha:
    if len(A) < K:
        pos = []
        for i, s in enumerate(S):
            if c == s:
                A.add(c)
                pos.append(i)
        dfs(c, pos)

A = list(A)
A.sort()
print(A[K - 1])
