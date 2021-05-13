# import itertools
# import math
# import sys
# import numpy as np

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# X, N = map(int, input().split())
# P = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

abcs = "abcdefghijklmnopqrstuvwxyz"
ans = ""
while(N > 0):
    # if N == 26:
    #     ans += "z"
    #     break
    N -= 1
    _ = N % 26
    # print(N % 26)
    N //= 26
    # print(N)
    ans += abcs[_]
    # print()

print(ans[::-1])
