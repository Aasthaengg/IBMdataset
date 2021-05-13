#!/usr/bin/env python3

def solve(n,h):
    ans = 0
    counter = 0
    memo = 0
    for i in range(n):
        if h[i] <= memo:
            counter += 1
        else:
            counter = 0
        memo = h[i]
        ans = max(ans,counter)
    return ans

def main():
    N = int(input())
    H = list(map(int,input().split()))
    print(solve(N,H))

if __name__ == '__main__':
    main()
