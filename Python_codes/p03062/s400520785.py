#create date: 2020-06-29 15:39

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    a = na()
    a_abs = list()
    zero = False
    minus = 0
    for ai in a:
        if ai < 0:
            minus += 1
        elif ai == 0:
            zero = True
        a_abs.append(abs(ai))
    
    if minus % 2 == 0 or zero:
        print(sum(a_abs))
    else:
        print(sum(a_abs) - 2 * min(a_abs))
        

if __name__ == "__main__":
    main()