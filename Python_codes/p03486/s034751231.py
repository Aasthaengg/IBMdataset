#!/usr/bin/env python3
S, T = input(), input()
s = "".join(sorted([i for i in S]))
t = "".join(sorted([i for i in T])[::-1])
print("YNeos"[s >= t::2])
