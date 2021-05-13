import sys
from math import log2
from math import ceil

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, k = MI()
    p = 0
    for i in range(1, min(n+1, k)):
        x = ceil(log2(k/i))
        p += 0.5**x
    p += max(0, n-k+1)
    p /= n
    print(p)

if __name__ == '__main__':
    main()