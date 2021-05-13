# -*- coding: utf-8 -*-

def count(data):
    even = odd = 0
    for val in data:
        if val % 2 == 0:
            even += 1
        else:
            odd += 1

    return even,odd

A,B,C = map(int, input().split())

ans = 0
even,odd = count([A, B, C])
if even == 2:
    ans += 1
    if A % 2 == 0:
        A += 1
    if B % 2 == 0:
        B += 1
    if C % 2 == 0:
        C += 1
elif odd == 2:
    ans += 1
    if A % 2 != 0:
        A += 1
    if B % 2 != 0:
        B += 1
    if C % 2 != 0:
        C += 1

max_val = max(A,B,C)

ans += (max_val - A) / 2
ans += (max_val - B) / 2
ans += (max_val - C) / 2
print(int(ans))
