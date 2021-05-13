import sys
import math
import bisect

def main():
    ans = 0
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ans += b - a + 1
    print(ans)

if __name__ == "__main__":
    main()
