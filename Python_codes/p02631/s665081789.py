#create date: 2020-06-29 22:59

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    a = na()
    a_xor = 0
    for ai in a:
        a_xor ^= ai
    for ai in a:
        print(a_xor^ai, end=" ")

if __name__ == "__main__":
    main()