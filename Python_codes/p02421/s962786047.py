# Aizu Problem ITP_1_9_C: String Game
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


taro, hanako = 0, 0
n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    if s1 == s2:
        taro += 1
        hanako += 1
    elif s1 > s2:
        taro += 3
    else:
        hanako += 3

print(taro, hanako)