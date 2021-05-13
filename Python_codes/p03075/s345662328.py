#!/usr/bin/env python3
# N = int(input())
# S = input()
d = []
for _ in range(5):
    d.append(int(input()))
if max(d) - min(d) <= int(input()):
    print("Yay!")
else:
    print(":(")

