
import sys
from sys import stdin
input = stdin.readline

n = int(input())
D = {}
for i in range(n):
    s = input()
    if s[0] == "i":
        D[s[7:]] = 11111111111111111111111111111111111
    else:
        print("yes" if s[5:] in D else "no")

