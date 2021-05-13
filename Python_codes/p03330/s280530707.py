import sys
input = sys.stdin.buffer.readline

def main():
    n, c = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(c)]
    C_ = [list(map(int, input().split())) for _ in range(n)]
    C = [0]*n
    for i, c_ in enumerate(C_):
        c_ = [x-1 for x in c_]
        C[i] = c_

    X = [[0]*c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            m = (i+j)%3
            X[m][C[i][j]] += 1

    #print(C)
    import itertools
    ans = 10**18
    for p in itertools.permutations(range(c), 3):
        temp = 0
        for i in range(3):
            for j in range(c):
                temp += D[j][p[i]]*X[i][j]
        ans = min(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()
