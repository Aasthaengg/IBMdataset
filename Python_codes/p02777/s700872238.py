import sys
import math
from collections import deque
from collections import defaultdict

def main():
    s, t = input().split()
    a, b = list(map(int,sys.stdin.readline().split()))
    u = input()
    if u == s:
        a -= 1
    else: b -= 1
    print(a,b)
    return 0

if __name__ == "__main__":
    main()