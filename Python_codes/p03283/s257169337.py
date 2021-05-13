def main():
    n, m, Q = map(int, input().split())
    Train= [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(m):
        l, r = map(int, input().split())
        l, r = l - 1, r - 1
        Train[l][r] += 1
    
    P_Train = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += Train[i][j]
            P_Train[i][j] = tmp

    for i in range(Q):
        p, q = map(int, input().split())
        p, q = p - 1, q - 1
        ans = solve(P_Train, n, p, q)
        print(ans)

def solve(P_Train, n, p, q):
    ans = 0
    for i in range(p, q + 1):
        if  p - 1 < 0:
            ans += P_Train[i][q]
        else:
            ans += P_Train[i][q] - P_Train[i][p - 1]
    return ans


if __name__ == '__main__':
    main()