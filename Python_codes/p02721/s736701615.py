#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, k, c = map(int, input().split())
s = list(input().rstrip())

to_work_f = set() 
to_work_b = set() 

rest = 0
for i, ch in enumerate(s):
    if rest == 0 and ch == "o":
        to_work_f.add(i)
        rest = c
    elif rest != 0:
        rest -= 1
rest = 0
for i, ch in enumerate(s[::-1]):
    if rest == 0 and ch == "o":
        to_work_b.add(n - i - 1)
        rest = c
    elif rest != 0:
        rest -= 1

if len(to_work_f) > k or len(to_work_b) > k:
    exit()
ans = []
for item in to_work_f:
    if item in to_work_b:
        ans.append(item + 1)
ans.sort()
for item in ans:
    print(item)