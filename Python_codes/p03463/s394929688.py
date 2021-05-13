from sys import stdin
import sys
import math

N, A, B = list(map(int, stdin.readline().rstrip().split()))


if (B - A) % 2 == 0:
    print("Alice")
elif (B - A) % 2 == 1:
    print("Borys")
