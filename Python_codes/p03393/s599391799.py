#!/usr/bin/env python3
import sys
input = sys.stdin.readline
from collections import Counter

s = input().rstrip()
n = len(s)
cnt = Counter(s)

for i in range(97, 97 + 26):
    key = chr(i)
    if key not in s:
        print(s + key)
        exit()

largest = s[-1]
seen = []
for i, ch in enumerate(s[::-1]):
    if ch < largest:
        for item in seen:
            if ch < item:
                s = s[:n-i-1] + item
                print(s)
                exit()
    largest = max(largest, ch)
    seen.append(ch)
    seen.sort()

print(-1)