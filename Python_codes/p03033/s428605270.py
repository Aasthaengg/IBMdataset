# https://atcoder.jp/contests/abc128/submissions/7097699
import sys
input = sys.stdin.readline

from bisect import bisect_left

n,q = map(int, input().split())
road = [list(map(int, input().split())) for i in range(n)]
road.sort(key=lambda x: x[2])
start = [int(input()) for i in range(q)]

skip = [-1]*q
ans = [-1]*q
for s,t,x in road:
    left = bisect_left(start, s-x)
    right = bisect_left(start, t-x)
    # [left, right)をxで埋める
    # すでに存在するところ(skipがあるところ)は飛ばす
    while left < right:
        if skip[left] == -1:
            ans[left] = x
            skip[left] = right
            left += 1
        else:
            left = skip[left]
print(*ans, sep="\n")