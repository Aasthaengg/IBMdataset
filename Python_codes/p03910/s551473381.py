#create date: 2020-08-07 07:40

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def check(k, n):
    a = k * (k + 1) // 2
    if n <= a:
        return True
    else:
        return False


def main():
    n = ni()

    # bisect
    l = 1; r = n
    while l + 1 < r:
        k = (l + r) // 2
        if check(k, n):
            r = k
        else:
            l = k
    
    no = r * (r + 1) // 2 - n
    for i in range(1, r+1):
        if i == no:
            continue
        print(i)

if __name__ == "__main__":
    main()