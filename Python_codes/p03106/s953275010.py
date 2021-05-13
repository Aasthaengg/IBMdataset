import sys
import math
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')


def main():
    A, B, K = map(int, readline().split())
    C = []
    for i in range(1,min(A,B)+1):
        if A%i==0 and B%i==0:
            C.append(i)

    print(C[-K])

if __name__ == '__main__':
    main()
