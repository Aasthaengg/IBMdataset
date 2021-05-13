# coding: utf-8

# https://atcoder.jp/contests/abc121


def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [None] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        left = C
        for j in range(M):
            left += A[i][j] * B[j]
        
        if left > 0:
            ans += 1
    
    return ans


print(main())
