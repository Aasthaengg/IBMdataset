# https://atcoder.jp/contests/abc122/tasks/abc122_c

import sys


def input():
    return sys.stdin.readline().strip()


n, q = [int(i) for i in input().split()]
S = input()

ac_table = [0] * (n + 1)  # その位置までにACが何個含まれているかを算出する。

prev = ""
for i in range(1, n + 1):
    if prev == "A" and S[i - 1] == "C":
        ac_table[i] = ac_table[i - 1] + 1
    else:
        ac_table[i] = ac_table[i - 1]
    prev = S[i - 1]

for _ in range(q):
    l, r = [int(i) for i in input().split()]
    print(ac_table[r] - ac_table[l])
