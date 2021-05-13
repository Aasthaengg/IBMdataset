#!/usr/bin/env python3
H, W = map(int, input().split())
a = ['#' * (W + 2)]
for i in range(H):
    a.append('#' + input() + '#')
a.append('#' * (W + 2))

for i in a:
    print(i)
