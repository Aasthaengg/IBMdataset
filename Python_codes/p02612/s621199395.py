#!/usr/bin/env python3
import sys


def solve(N: int):
    answer = 1000 - (N % 1000)
    if answer == 1000:
        answer = 0
    return answer

def main():
    N = int(input())  # type: int
    answer = solve(N)
    print(answer)

if __name__ == '__main__':
    main()
