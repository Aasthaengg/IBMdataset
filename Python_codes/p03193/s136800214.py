from sys import stdin, stdout
import math
import bisect
import queue

N,H,W = map(int,stdin.readline().strip().split())

ans = 0

for i in range(N):
    A, B = map(int, stdin.readline().strip().split())
    ans += min(A // H, B // W)

stdout.writelines(str(ans) + '\n')
