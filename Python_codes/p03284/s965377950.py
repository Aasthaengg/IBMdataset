#!/usr/bin/env python3

def solve(N: int, K: int):
    d = int(N % K)
    if d == 0:
      print(d)
    else:
      print(1)
    return

def main():
    N, K = map(int, input().split())
    solve(N, K)

if __name__ == '__main__':
    main()