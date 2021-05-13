import sys
import math
import bisect


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(n):
        A[i] -= B[i]
    ans = 0
    for a in A:
        if a > 0:
            ans += a
    print(ans)

if __name__ == "__main__":
    main()
