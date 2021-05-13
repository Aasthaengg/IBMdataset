#create date: 2020-07-03 18:05

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    k, x = na()
    amin, amax = x-k+1, x+k-1
    print(*list(range(amin, amax+1)))

if __name__ == "__main__":
    main()