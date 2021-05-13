#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    i = 0
    while 1:
        if i == N:
            break
        # 単調非減少と単調非増加の列の長い方を採用Greedy
        a = i
        while a < N-1 and A[a] <= A[a+1]:
            a += 1
        b = i
        while b < N-1 and A[b] >= A[b+1]:
            b += 1
        i = max(a,b) + 1
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
