#!/usr/bin/env python3
s = input()
n = -(-(len(s) - 1) // 2)
print(sum(i != j for i, j in zip(s[:n], s[-n:][::-1])))
