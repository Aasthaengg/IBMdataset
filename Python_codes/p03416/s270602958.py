import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        s = str(i)
        if s == s[::-1]:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
