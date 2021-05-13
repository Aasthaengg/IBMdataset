import sys
import math
import bisect

def main():
    n = int(input())
    ans = []
    ans.append('Christmas')
    for i in range(25 - n):
        ans.append('Eve')
    print(' '.join(ans))

if __name__ == "__main__":
    main()
