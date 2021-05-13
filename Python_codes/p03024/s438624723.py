#!/usr/bin/env python3
s = input()
victory = s.count("o")
if 15 - len(s) + victory >= 8: print("YES")
else: print("NO")