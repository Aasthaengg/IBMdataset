import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M, Q = map(int, input().split())

    """
    １からの遷移に分解する系の発想なのかなあ
    table[s][t] = (sスタートでtエンドの列車本数)
    として２次元テーブルを用意しておけば、クエリ(p, q)に対する解は
        sum(table[ps:q][p:q])
    で彫られ、これは２次元累積和で高速計算可能。
    """

    table = [[0] * N for _ in range(N)]
    for _ in range(M):
        l, r = map(int, input().split())
        table[l - 1][r - 1] += 1

    for j in range(1, N):
        table[0][j] += table[0][j - 1]
    for i in range(1, N):
        summation = 0
        for j in range(N):
            summation += table[i][j]
            table[i][j] = table[i - 1][j] + summation

    for _ in range(Q):
        p, q = map(int, input().split())
        p, q = p - 1, q - 1
        if p == 0:
            print(table[q][q])
        else:
            print(table[q][q] - table[p - 1][q] - table[q][p - 1] + table[p - 1][p - 1])

if __name__ == "__main__":
    main()
