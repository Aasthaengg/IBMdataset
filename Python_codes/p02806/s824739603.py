# -*- coding: utf-8 -*-

N = int(input())
s = list()
t = list()
for i in range(N):
    _s, _t = map(str, input().split())
    s.append(_s)
    t.append(int(_t))
X = input()

ans = 0
for i in range(s.index(X) + 1, N):
    ans += t[i]

print(ans)
