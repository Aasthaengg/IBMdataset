#!/usr/bin/env python3
import sys

def main():
    N, M, K = map(int, input().split())
    for i in range(N+1):
        a = K - i * M
        b = N - 2*i
        if b == 0:
            if K == i*M:
                print('Yes')
                exit()
        elif a % b == 0 and 0 <= a // b <= M:
            print('Yes')
            exit()
    print('No')
            

if __name__ == '__main__':
    main()
