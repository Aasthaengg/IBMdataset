import sys
import numpy as np
input = sys.stdin.readline

def main():
    N = 50
    K = int(input())
    # K = 50 * int(1e16)
    tmp = K // N
    K %= N
    a = np.array([i for i in range(N)])
    for i in range(K):
        a -= 1
        a[i] += N + 1
    print(N)
    for i in range(N-1):
        print(a[i]+tmp, end=" ")
    print(a[N-1]+tmp)

if __name__ == "__main__":
    main()