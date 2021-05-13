# coding: utf-8
import math
N, M = map(int,input().split())
#N = int(input())
#K = int(input())
#S = input()
ans = 0
#l = list(map(int,input().split()))
#A = list(map(int,input().split()))
F = [False] * (N+1)
pen = 0
P = [0] * (N+1)
for i in range(M):
    p, s = map(str,input().split())
    p = int(p)
    if s == "WA" and not F[p]:
        P[p] += 1
    if s == "AC" and not F[p]:
        ans += 1
        pen += P[p]
        F[p] = True

print(ans, pen)