#!/usr/local/bin/python3
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

N = int(input())
ans_cand = int(N / 1.08)
if int((ans_cand) * 1.08) == N:
    print(ans_cand)
elif int((ans_cand+1) * 1.08) == N:
    print(ans_cand+1)
elif int((ans_cand-1) * 1.08) == N:
    print(ans_cand-1)
else:
    print(":(")
