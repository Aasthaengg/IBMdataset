import sys
input = sys.stdin.readline

N, P = map(int, input().split())

if P == 1:
    print(0)
else:
    print(N - P)