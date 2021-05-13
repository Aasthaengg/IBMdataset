import sys

input = lambda :sys.stdin.readline().rstrip()

def main():
    n, m, Q = map(int, input().split())
    Train= [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(m):
        l, r = map(int, input().split())
        l, r = l - 1, r - 1
        Train[l][r] += 1
    
    P_Train = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            P_Train[i + 1][j + 1] = P_Train[i][j + 1] + P_Train[i + 1][j] + Train[i][j] - P_Train[i][j]
    
    #print(*P_Train, sep = '\n')

    for i in range(Q):
        p, q = map(int, input().split())
        p, q = p - 1, q - 1
        ans = solve(P_Train, p, q)
        print(ans)

def solve(P_Train, p, q):
    ans = 0
    ans = P_Train[q + 1][q + 1] -P_Train[p][q + 1] - P_Train[q + 1][p] + P_Train[p][p]
    return ans


if __name__ == '__main__':
    main()