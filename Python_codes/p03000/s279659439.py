import sys

N, X = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

ans = 0
for i, l in enumerate(L):
    ans += l
    if ans > X:
        print(i+1)
        break
else:
    print(N+1)