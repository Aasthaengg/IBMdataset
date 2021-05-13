N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

Pt = max([S.count(s)-T.count(s) for s in S])

print(max(0, Pt))