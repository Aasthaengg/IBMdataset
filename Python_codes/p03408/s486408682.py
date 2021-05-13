N = int(input())
S = [input() for n in range(N)]
M = int(input())
T = [input() for m in range(M)]
print(max(0,max([S.count(s)-T.count(s) for s in S])))