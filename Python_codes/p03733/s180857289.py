# from pprint import pprint
# import math
# import collections

# n = int(input())
N, T = map(int, input().split(' '))
t = list(map(int, input().split(' ')))

total = 0
for i in range(N):
    if i > 0:
        total += min(T, t[i]-t[i-1])

    # print(i, total)
total += T

print(total)
