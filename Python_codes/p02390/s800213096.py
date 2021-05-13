#!/usr/bin/env python3
s = int(input())
h, m, s = int(s / 3600), int(s / 60) % 60, s % 60
print(h, m, s, sep=':')