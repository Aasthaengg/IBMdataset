import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        a, b = map(int, input().split())
        if b <= m:
            A.append(a)
    if len(A) == 0:
        print('TLE')
    else:
        print(min(A))

if __name__ == "__main__":
    main()
