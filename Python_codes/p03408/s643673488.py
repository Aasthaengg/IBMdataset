N = int(input())
S = [input() for n in range(N)]
M = int(input())
T = [input() for m in range(M)]
A = [0]

for s in S:
  A.append(S.count(s)-T.count(s))

print(max(A))