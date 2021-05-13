#create date: 2020-08-10 07:31

import sys
stdin = sys.stdin
import math

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b = ns().split(" ")
    n = int(a+b)
    if math.sqrt(n).is_integer():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()