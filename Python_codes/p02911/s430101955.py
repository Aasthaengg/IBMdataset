import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, K, Q = map(int, input().split())
    vals = np.array([K for _ in range(N)])
    for _ in range(Q):
        A = int(input())
        vals -= 1
        vals[A-1] += 1
    for v in vals:
        if v > 0:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
