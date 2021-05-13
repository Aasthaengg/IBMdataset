#create date: 2020-07-20 13:34

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    p = na()
    ans = 0
    for i in range(1, n-1):
        a = p[i-1:i+2]
        if p[i] != max(a) and p[i] != min(a):
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    main()