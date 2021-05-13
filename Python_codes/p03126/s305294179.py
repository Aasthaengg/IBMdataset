# coding: utf-8

# https://atcoder.jp/contests/abc118


def main():
    N, M = map(int, input().split())
    k_a = [None] * N
    for i in range(N):
        k_a[i] = list(map(int, input().split()))
    
    food = [0] * (M+1)
    for i in range(N):
        for j in range(1, k_a[i][0]+1):
            food[k_a[i][j]] += 1
    
    ans = 0
    for m in range(1, M+1):
        if food[m] == N:
            ans += 1
    
    return ans


print(main())
