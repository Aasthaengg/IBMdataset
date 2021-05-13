#create date: 2020-07-05 10:48

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    p = na()
    for i in range(n-1):
        for j in range(i, n):
            q = p.copy()
            q[i] = p[j]; q[j] = p[i]
            now = q[0]
            f = True
            for qi in q:
                if now > qi:
                    f = False
                    break
                now = qi
            if f:
                print("YES")
                quit()
    print("NO")



if __name__ == "__main__":
    main()