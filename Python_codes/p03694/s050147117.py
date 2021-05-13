import sys
import math
import bisect

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = max(A) - min(A)
    print(ans)

if __name__ == "__main__":
    main()
