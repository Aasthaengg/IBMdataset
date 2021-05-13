import sys
readline = sys.stdin.readline

N = int(readline())
X = list(map(int,readline().split()))

S = sorted(X)
mM = S[N // 2 - 1]
lM = S[N // 2]

for i in range(N):
  if X[i] <= mM:
    print(lM)
  else:
    print(mM)
