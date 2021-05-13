import sys
sys.setrecursionlimit(5 * 10**5)
input = sys.stdin.readline

X, Y = list(map(int, input().split()))

if X % Y == 0:
    print(-1)
else:
    print(X)

