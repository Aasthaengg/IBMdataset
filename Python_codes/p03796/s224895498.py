import sys
import math
import bisect

def main():
    n = int(input())
    m = 10 ** 9 + 7
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i % m
    print(ans)

if __name__ == "__main__":
    main()
