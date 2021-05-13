if __name__ == '__main__':
    N, M = map(int, input().split())
    beki =1
    for i in range(M):
        beki *= 2
    ans = beki * (M * 1900 + (N-M) * 100)
    print(ans)