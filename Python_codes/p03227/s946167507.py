#!/usr/bin/env python3
S = input()
print(S[::-1 if len(S) % 2 else 1])
