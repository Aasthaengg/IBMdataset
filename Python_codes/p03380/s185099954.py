#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    A_max = A_sorted[-1]
    A = A_sorted[:-1]
    tansaku = (A_max + 1) // 2
    ok = 0
    ng = len(A) - 1
    if A[ok] > tansaku:
        print(A_max, A[ok])
        exit()
    if A[ng] <= tansaku:
        print(A_max, A[ng])
        exit()
    while ok + 1 < ng:
        center = (ok + ng) // 2
        if A[center] <= tansaku:
            ok = center
        else:
            ng = center
    if tansaku - A[ok] <= A[ng] - tansaku:
        print(A_max, A[ok])
    else:
        print(A_max, A[ng])

if __name__ == "__main__":
    main()