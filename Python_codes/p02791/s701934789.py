# import itertools
# import math

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# N, M = map(int, input().split())
P = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()


min = 999999999
cnt = 0
for i in P:
    if min >= i:
        cnt += 1
        min = i

print(cnt)