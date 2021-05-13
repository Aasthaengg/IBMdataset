#!/usr/bin/env python3
n = int(input())
k = int(input())
x = list(map(int, input().split()))

cnt = 0

for i in x:
    if i <= (k / 2):
        cnt += i * 2
    else:
        cnt += (k - i) * 2

print(cnt)
