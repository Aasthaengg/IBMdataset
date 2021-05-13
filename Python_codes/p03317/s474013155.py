#!/usr/bin/env python3
import sys

def main():
    N, K = map(int,input().split())
    a = list(map(int,input().split()))

    answer = 0
    for i in range(N):
        if K + (i-1)*(K-1) >= N:
            answer = i
            break

    print(answer)
    return

if __name__ == '__main__':
    main()
