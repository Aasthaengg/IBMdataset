#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
a = [int(x) for x in input().split()]
xor = 0
for x in a:
    xor ^= x
print(*(xor ^ x for x in a))