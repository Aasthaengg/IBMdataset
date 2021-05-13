def resolve():
    '''
    code here
    '''
    N, M, C = [int(item) for item in input().split()]
    Bs = [int(item) for item in input().split()]

    grid = [[int(item) for item in input().split()] for _ in range(N)]

    cnt = 0

    for i in range(N):
        temp = C
        for j in range(M):
            temp += grid[i][j]*Bs[j]
        if temp > 0:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
