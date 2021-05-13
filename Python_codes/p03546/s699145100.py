from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
INF = 1 << 60


def input():
    return stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if C[i][j] > C[i][k] + C[k][j]:
                    C[i][j] = C[i][k] + C[k][j]
                    
    ans = 0
    for row in A:
        for n in row:
            if n != -1:
                ans += C[n][1]
    
    print(ans)
    return


if __name__ == '__main__':
    main()
