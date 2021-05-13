import sys


def input():
    return sys.stdin.readline()[:-1]


N, K = map(int, input().split())
ab = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    ab.append(tmp)
ab.sort()

cnt = 0
for i in range(N):
    cnt += ab[i][1]
    if cnt >= K:
        print(ab[i][0])
        exit(0)
