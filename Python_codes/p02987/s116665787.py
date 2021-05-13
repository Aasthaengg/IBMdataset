#create date: 2020-07-12 13:28

import sys
stdin = sys.stdin
from collections import Counter

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    s = ns()
    lc = list(Counter(s).values())
    if len(lc) == 2 and lc[0] ==lc[1]:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()