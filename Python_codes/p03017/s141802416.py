import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n, a, b, c, d = map(int, input().split())
    s = input()
    for i in range(a, max(c,d)):
        if s[i-1:i+1] == "##":
            print("No")
            exit()
    if c < d:
        print("Yes")
        exit()
    for i in range(b-1, d):
        if s[i-1:i+2] == "...":
            print("Yes")
            exit()
    print("No")
    return 0

if __name__ == "__main__":
    solve()