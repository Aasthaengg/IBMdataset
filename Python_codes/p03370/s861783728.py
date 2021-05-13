import sys
import math
import bisect

def solve(A, m):
    n = len(A)
    ans = n
    m -= sum(A)
    ans += m // min(A)
    return ans

def main():
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        A.append(int(input()))
    print(solve(A, m))

if __name__ == "__main__":
    main()
