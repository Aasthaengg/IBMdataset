import itertools
N = int(input())
X = [input()[0] for _ in range(N)]
M = X.count("M")
A = X.count("A")
R = X.count("R")
C = X.count("C")
S = 0
H = X.count("H")
for s in itertools.combinations([M, A, R, C, H], 3):
  S += s[0]*s[1]*s[2]
print(S)