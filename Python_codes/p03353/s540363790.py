import sys
from collections import Counter

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    s = input()
    N = len(s)
    K = ii()

    A = set()
    for i in range(N):
        for j in range(K):
            A.add(s[i:i+j+1])
    A = list(A)
    A.sort()
    print(A[K-1])


if __name__ == '__main__':
    main()
