#create date: 2020-07-03 16:23

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    c = na()
    dif1, dif2 = c[1] - c[0], c[2] - c[1]
    for i in range(2):
        cn = na()
        if cn[1] - cn[0] != dif1 or cn[2] - cn[1] != dif2:
            print("No")
            quit()
    print("Yes")

if __name__ == "__main__":
    main()