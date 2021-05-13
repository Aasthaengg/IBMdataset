#create date: 2020-08-07 07:31

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()

    ans = [0] * (10**8 + 1)
    for x in range(1, 10**2+1):
        for y in range(1, 10**2+1):
            for z in range(1, 10**2+1):
                k = x**2 + y**2 + z**2 + x*y + y*z + z*x
                ans[k] += 1
    for k in range(1, n+1):
        print(ans[k])

if __name__ == "__main__":
    main()