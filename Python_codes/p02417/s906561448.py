from __future__ import division, print_function
from sys import stdin
cnt = [0] * 127
for c in stdin.read().lower():
    cnt[ord(c)] += 1
for i in range(ord('a'), ord('z')+1):
    print(chr(i), ':', cnt[i])