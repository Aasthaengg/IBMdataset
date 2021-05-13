import sys
import math
import bisect

def solve(a, b, k):
    ans = []
    for i in range(k):
        if a + i <= b:
            ans.append(a + i)
        if b - i >= a:
            ans.append(b - i)
    ans = sorted(set(ans))
    return ans

def main():
    a, b, k = map(int, input().split())
    for a in solve(a, b, k):
        print(a)

if __name__ == "__main__":
    main()
