import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

sort = sorted(X)
first = sort[N//2 - 1]
second = sort[N//2]

for i in range(N):
    if X[i] <= first:
        print(second)
    else:
        print(first)