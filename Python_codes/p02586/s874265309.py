def main():
    R, C, K = map(int, input().split())
    matrix = [[0] * (C+1) for i in range(R+1)]
    for k in range(K):
        ri, ci, vi = map(int, input().split())
        matrix[ri][ci] = vi
    # print(matrix)
    dp0 = [[0] * (C+1) for _ in range(R+1)]
    dp1 = [[0] * (C+1) for _ in range(R+1)]
    dp2 = [[0] * (C+1) for _ in range(R+1)]
    dp3 = [[0] * (C+1) for _ in range(R+1)]
    
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            tmp = matrix[r][c]
            if tmp == 0:
                dp0[r][c] = max(dp0[r][c-1], dp0[r-1][c], dp1[r-1][c], dp2[r-1][c], dp3[r-1][c])
                dp1[r][c] = dp1[r][c-1]
                dp2[r][c] = dp2[r][c-1]
                dp3[r][c] = dp3[r][c-1]
            else:
                dp0[r][c] = max(dp0[r][c-1], dp0[r-1][c], dp1[r-1][c], dp2[r-1][c], dp3[r-1][c])
                dp1[r][c] = max(dp0[r][c-1] + tmp, dp1[r][c-1], 
                                dp0[r-1][c] + tmp, dp1[r-1][c] + tmp, dp2[r-1][c] + tmp, dp3[r-1][c] + tmp)
                dp2[r][c] = max(dp1[r][c-1] + tmp, dp2[r][c-1])
                dp3[r][c] = max(dp2[r][c-1] + tmp, dp3[r][c-1])

    print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))
    
main()
