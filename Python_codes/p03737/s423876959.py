import sys
import math
import bisect

def main():
    A = input().split()
    ans = []
    for a in A:
        ans.append(a[0].upper())
    print(''.join(ans))

if __name__ == "__main__":
    main()
