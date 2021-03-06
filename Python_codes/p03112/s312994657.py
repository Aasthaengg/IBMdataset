#!/usr/bin/env python3
from bisect import bisect_right

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    # print(s,t)
    s = [-10**12] + s + [10**12]
    t = [-10**12] + t + [10**12]

    for _ in range(Q):
        x = int(input())
        i = bisect_right(s,x)
        j = bisect_right(t,x)
        # print(i,j,x)
        ans = []

        ans.append(max(abs(s[i-1] - x), abs(t[j-1] - x)))
        ans.append(max(abs(s[i] - x), abs(t[j] - x)))
        ans.append(abs(s[i-1] - x) + abs(t[j] - x) + min(abs(s[i-1]-x), abs(t[j]-x)))
        ans.append(abs(s[i] - x) + abs(t[j-1] - x) + min(abs(s[i]-x), abs(t[j-1]-x)))

        print(min(ans))

if __name__ == "__main__":
    main()
