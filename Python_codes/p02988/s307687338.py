import sys
import math
import bisect

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if A[i] == sorted([A[i-1], A[i], A[i+1]])[1]:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
