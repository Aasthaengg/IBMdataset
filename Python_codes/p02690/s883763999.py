#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


X = I()

for a in range(-118, 120):
    for b in range(-119, 119):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit()
