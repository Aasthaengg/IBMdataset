def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    
    import copy
    D = [[[0,1] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            D[i][j][0] = A[i][j]
    flag = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if k != i and k != j:
                    if D[i][j][0] > D[i][k][0] + D[k][j][0]:
                        flag = 1
                    elif D[i][j][0] == D[i][k][0] + D[k][j][0]:
                        D[i][j][1] += 1
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if D[i][j][1] == 1:
                ans += D[i][j][0]
    if flag == 1:
        print(-1)
    else:
        print(ans)
    
main()