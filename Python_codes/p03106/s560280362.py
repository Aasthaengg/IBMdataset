#! /usr/bin/env python3
a, b, c = map(int, input().split())
t = []
for i in range(1, 101):
    if a%i + b%i < 1: t += [i]
print(t[-c])