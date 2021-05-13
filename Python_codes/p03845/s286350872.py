import sys

N = int(input())
T = list(map(int, sys.stdin.readline().rsplit()))
M = int(input())

sumT = sum(T)
for _ in range(M):
    p, x = map(int, input().split())
    t = T[p - 1]
    print(sumT - (t - x))
