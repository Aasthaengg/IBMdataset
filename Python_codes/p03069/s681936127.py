# author:  Taichicchi
# created: 26.09.2020 14:35:45

import sys

N = int(input())

S = input()

ls_l = [0]
ls_r = [0]

for i in range(N):
    if S[i] == "#":
        ls_l.append(ls_l[-1] + 1)
    else:
        ls_l.append(ls_l[-1])

for i in range(N)[::-1]:
    if S[i] == ".":
        ls_r.append(ls_r[-1] + 1)
    else:
        ls_r.append(ls_r[-1])

ls_r.reverse()

# print(ls_l)
# print(ls_r)

ans = 10 ** 6

for i in range(N + 1):
    ans = min(ans, ls_l[i] + ls_r[i])

print(ans)
