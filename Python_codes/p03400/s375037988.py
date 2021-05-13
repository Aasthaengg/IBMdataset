#!/usr/bin/env python3

def f(d,m):
    return 1 + (d-1)//m

def solve(d,x,a):
    ans = x
    for i in range(len(a)):
        ans += f(d,a[i])
    return ans



def main():
    N = int(input())
    D,X = map(int,input().split())
    a = [int(input()) for _ in range(N)]
    print(solve(D,X,a))


if __name__ == '__main__':
    main()
