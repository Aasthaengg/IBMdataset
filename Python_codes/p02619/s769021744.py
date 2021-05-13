#create date: 2020-06-28 21:05

import sys
stdin = sys.stdin
import numpy as np

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    d = ni()
    c = np.array(na())
    s = list()
    for i in range(d):
        a = na()
        s.append(a)
    t = list()
    for i in range(d):
        t.append(ni()-1)

    period = np.zeros(26)
    last_day = np.zeros(26)
    v = 0

    for day in range(1, d+1):
        last_day[t[day-1]] = day
    
        v += s[day-1][t[day-1]]
        v -= (sum(c * (day - last_day)))
        print(int(v))
        
if __name__ == "__main__":
    main()