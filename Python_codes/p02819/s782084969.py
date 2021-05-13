#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

def main():
    X = int(input())
    for i in range(X, 10**8):
        if is_prime(i):
            print(i)
            exit()

if __name__ == '__main__':
    main()
