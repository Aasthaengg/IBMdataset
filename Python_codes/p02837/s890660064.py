#!/usr/bin/env python3]
import sys
sys.setrecursionlimit(2000)

N = int(input())
syogen = []
for i in range(N):
    N_a = int(input())
    syogen_a = []
    for _ in range(N_a):
        x, y = input().split()
        syogen_a.append([int(x) - 1, int(y)])
    syogen.append(syogen_a)


def syojiki(i):
    for x, y in syogen[i]:
        if y == 1:
            syojiki_list.append(x)
            if len(syojiki_list) >= N:
                return
            syojiki(x)


def check_syojiki(syojikitati):
    d = {}
    for s in range(N):
        if s in syojikitati:
            d[s] = 1
        else:
            d[s] = 0

    for s in syojikitati:
        d[s] = 1
        for x, y in syogen[s]:
            if d[x] != y:
                return False
    return True


max_syojiki = 0

for i in range(2 ** N):
    d = {}
    syojiki_list = []
    for j in range(N):
        if (i >> j) & 1:
            syojiki_list.append(j)
            syojiki(j)
    syojiki_list = list(set(syojiki_list))
    if check_syojiki(syojiki_list):
        max_syojiki = max(max_syojiki, len(syojiki_list))

print(max_syojiki)
