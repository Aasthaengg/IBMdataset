#create date: 2020-03-18 07:40

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b, k = na()
    for i in range(k):
        b += a//2
        a //= 2
        a, b = b, a
    if k % 2 == 1:
        a, b = b, a
    print(a, b)

if __name__ == "__main__":
    main()