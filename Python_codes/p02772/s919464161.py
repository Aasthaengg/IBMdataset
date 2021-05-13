# -*- coding: utf-8 -*-
N = int(input())
A = map(int, input().split())

for a in A:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            continue
        print("DENIED")
        exit()
print("APPROVED")
