def main():
    N, A, B, C = (int(_) for _ in input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10 ** 12

    def dfs(i, a, b, c):
        if i == N:
            return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a, b, c) > 0 else INF
        c0 = dfs(i+1, a, b, c)
        c1 = dfs(i+1, a+L[i], b, c) + 10
        c2 = dfs(i+1, a, b+L[i], c) + 10
        c3 = dfs(i+1, a, b, c+L[i]) + 10
        return min(c0, c1, c2, c3)

    print(dfs(0, 0, 0, 0))
    return

if __name__ == '__main__':
    main()
