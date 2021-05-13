from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi

MOD = 10 ** 9 + 7
SIZE = 10 ** 6

N, P = map(int, input().split())
S = input()

answer = 0
if P == 2 or P == 5:
    for i, s in enumerate(S):
        if int(s) % P == 0:
            answer += i + 1
else:
    S = S[::-1]
    cnt = defaultdict(int)
    tmp = 0
    for i, s in enumerate(S):
        tmp += int(s) * pow(10, i, P)
        if tmp % P == 0:
            answer += 1
        answer += cnt[tmp % P]
        cnt[tmp % P] += 1

print(answer)