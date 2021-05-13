#!/usr/bin/env python3
s = input()
print("yneos"[len(s) != len(set(i for i in s))::2])
