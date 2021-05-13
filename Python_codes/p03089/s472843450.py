#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    b = list(map(int, input().split()))
    ans = []
    for i in range(N):
        pos = 0
        for j in range(N-i):
            tmp = j+1 - b[j]
            if tmp < 0:
                print(-1)
                exit()
            elif tmp == 0:
                pos = j
        ans.append(b.pop(pos))
    for a in ans[::-1]:
        print(a)

if __name__ == '__main__':
    main()
