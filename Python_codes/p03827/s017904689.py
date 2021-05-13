#!/usr/bin/env python3
_, s = open(0).read().split()

print(
    max([sum(1 if i == "I" else -1 for i in s[:j+1])
         for j in range(int(_))] + [0]))
