#!/usr/bin/env python3
input()
a = map(int, input().split())
c = [0] * 9
for i in a:
    c[min(8, i // 400)] += 1
s = sum(i > 0 for i in c[:8])
print(max(s, 1), s + c[8])
