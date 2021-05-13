def main():
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(2)]

    right = 0
    under = 0
    ans = A[0][0] + A[1][N-1]
    temp = 0
    for i in range(N):
        for j in range(1,i+1):
            temp += A[0][j]

        for k in range(i,N-1):
            temp += A[1][k]

        judge = A[0][0] + A[1][N-1] + temp
        if judge > ans:
            ans = judge

        judge = 0
        temp = 0

    return ans

print(main())
