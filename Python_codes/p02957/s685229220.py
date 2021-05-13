#create date: 2020-07-05 10:44

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b = na()
    if a > b:
        a, b = b, a
    if (b - a) % 2 != 0:
        print("IMPOSSIBLE")
        quit()
    else:
        print(a + (b-a)//2)
if __name__ == "__main__":
    main()