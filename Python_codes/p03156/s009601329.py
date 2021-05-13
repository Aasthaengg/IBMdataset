#!/usr/bin/env python3

n = int(input())
a, b = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
p1 = [x for x in p if x <= a]
p2 = [x for x in p if a < x <= b]
p3 = [x for x in p if b < x]
r = [len(p1), len(p2), len(p3)]
print(min(r))
