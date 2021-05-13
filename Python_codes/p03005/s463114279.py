from collections import defaultdict
from collections import deque
from string import ascii_uppercase
import sys, bisect, math, heapq

stdin = sys.stdin
read_int = lambda : list(map(int,stdin.readline().split()))
read_str = lambda : stdin.readline().rstrip()

N, K = read_int()

def solve():
    if K == 1:
        return 0
    ans = N - K
    return ans

if __name__ == "__main__":
    print(solve())