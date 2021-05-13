#create date: 2020-06-29 13:35

import sys
stdin = sys.stdin
from collections import deque

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    k = ni()
    q = deque(map(str, range(1, 10)))
    for i in range(k):
        n = q.popleft()
        last_n = n[-1]
        for diff in range(-1, 2):
            next_n = int(last_n) + diff
            if next_n >= 0 and next_n <= 9:
                q.append(n+str(next_n))
    print(n)
if __name__ == "__main__":
    main()