#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    diff = sum(A) - sum(B)
    if diff < 0:
        print(-1)
    else:
        C = []
        for i in range(N):
            tmp = A[i] - B[i]
            if tmp >= 0:
                C.append(tmp)
        C.sort()
        # print(C,diff)
        j = 0
        while C[j] <= diff:
            diff -= C[j]
            j += 1
            if j == N:
                break
        print(N-j)

if __name__ == '__main__':
    main()
