#!/usr/bin/env python3
n, *b = map(int, open(0).read().split())
b = [b[0]] + b + [b[-1]]

print(sum(min(b[i], b[i + 1]) for i in range(n)))
