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

    #print(C)
    L = [[0]*c for _ in range(3)]
    for k in range(c):
        for i in range(n):
            for j in range(n):
                m = (i+j)%3
                x = C[i][j]
                L[m][k] += D[x][k]
                
    X = [[] for _ in range(3)]
    for j in range(3):
        for i, x in enumerate(L[j]):
            X[j].append((x, i))
    for i, x in enumerate(X):
        x.sort()
        x = x[0:3]
        X[i] = x

    #print(X)
    import itertools
    ans = 10**18
    for p in itertools.product(range(3), repeat=3):
        used_col = set()
        temp = 0
        for j in range(3):
            x, i =X[j][p[j]]
            if i in used_col:
                break
            else:
                temp += x
                used_col.add(i)
        else:
            ans = min(temp, ans)
    print(ans)

if __name__ == '__main__':
    main()
