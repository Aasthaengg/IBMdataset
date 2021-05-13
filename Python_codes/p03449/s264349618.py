#!/usr/bin/env python3

def solve(n,a):
    l = [0]*n
    for i in range(n):
        l[i] = sum(a[0][:i+1]) + sum(a[1][i:])
    return max(l)


def main():
    N = int(input())
    a = [list(map(int,input().split())) for _ in range(2)]
    print(solve(N,a))

if __name__ == '__main__':
    main()