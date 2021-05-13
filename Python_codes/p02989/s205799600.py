#create date: 2020-07-20 13:38

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    d = na()
    d.sort()
    dl = d[n//2-1]
    dr = d[n//2]
    if dl == dr:
        print(0)
    else:
        print(dr - dl)

if __name__ == "__main__":
    main()