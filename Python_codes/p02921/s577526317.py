import sys
import math
import bisect

def solve(s, t):
    ans = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += 1
    return ans

def main():
    print(solve(input(), input()))

if __name__ == "__main__":
    main()
