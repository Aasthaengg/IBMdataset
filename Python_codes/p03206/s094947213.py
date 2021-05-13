#create date: 2020-06-30 09:01

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    d = ni()
    print("Christmas" + " Eve" * (25-d))

if __name__ == "__main__":
    main()