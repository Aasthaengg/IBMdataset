#create date: 2020-08-10 07:34

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a = na()
    a.sort()
    zero = False
    for ai in a:
        if ai % 2== 0:
            zero =True
    print(0 if zero else a[0]*a[1])

if __name__ == "__main__":
    main()