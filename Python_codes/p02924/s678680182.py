import os, sys, re, math

N = int(input())

s = (1 + (N - 1)) * (N // 2)
if (N - 1) % 2 == 1:
    s -= N // 2

print(s)
