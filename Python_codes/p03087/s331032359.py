# author:  Taichicchi
# created: 12.09.2020 19:26:19

import sys

N, Q = map(int, input().split())

S = input()

cum_ls = [0]

for i in range(1, N):
    if S[i - 1: i + 1] == "AC":
        cum_ls.append(cum_ls[i - 1] + 1)
    else:
        cum_ls.append(cum_ls[i - 1])

# print(cum_ls)

for i in range(Q):
    l, r = map(int, input().split())
    print(cum_ls[r - 1] - cum_ls[l - 1])
