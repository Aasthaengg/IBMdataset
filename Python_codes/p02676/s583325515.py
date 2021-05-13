#create date: 2020-07-01 11:48

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    k = ni()
    s = ns()
    n = len(s)
    if n <= k:
        print(s)
    else:
        print(s[:k] + "...")

if __name__ == "__main__":
    main()