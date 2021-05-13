#!/usr/local/bin/python3
# https://atcoder.jp/contests/agc040/tasks/agc040_a

ans = 0
S = input().replace('><', '>,<').split(',')
for s in S:
    n = s.count('<')
    m = s.count('>')
    ans += (n*(n-1))//2 + (m*(m-1))//2 + max(n, m)

print(ans)
