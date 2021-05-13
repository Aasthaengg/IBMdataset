#!/usr/bin/env python3

def main():
    N = int(input())
    T = list(map(int,input().split()))
    M = int(input())
    t = sum(T)
    for _ in range(M):
        p,x = map(int,input().split())
        s = t - T[p-1] + x
        print(s)


if __name__ == '__main__':
    main()