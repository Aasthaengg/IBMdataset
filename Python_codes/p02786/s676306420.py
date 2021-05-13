import os, sys, re, math

memo = {}
def attack(h):
    result = memo.get(h)
    if result:
        return result
    if h == 1:
        result = 1
    else:
        result = 1 + attack(h // 2) * 2
    memo[h] = result
    return result

H = int(input())

print(attack(H))
