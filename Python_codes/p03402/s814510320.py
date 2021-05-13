def resolve():
    A, B = list(map(int, input().split()))
    K = 50
    grid = [["." for _ in range(2*K)] for __ in range(K)]
    grid += [["#" for _ in range(2*K)] for __ in range(K)]
    acnt = 1
    bcnt = 1
    for i in range(0, K-1):
        if bcnt >= B:
            break
        for j in range(2*K):
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                if 0 <= i+di <= 2*K-1 and 0 <= j+dj <= 2*K-1:
                    if grid[i+di][j+dj] == "#":
                        break
            else:
                grid[i][j] = "#"
                bcnt += 1
                if bcnt >= B:
                    break
    
    for i in range(K+1, 2*K):
        if acnt >= A:
            break
        for j in range(2*K):
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                if 0 <= i+di <= 2*K-1 and 0 <= j+dj <= 2*K-1:
                    if grid[i+di][j+dj] == ".":
                        break
            else:
                grid[i][j] = "."
                acnt += 1
                if acnt >= A:
                    break
    print(2*K, 2*K)
    [print("".join(grid[i])) for i in range(2*K)]
    
if '__main__' == __name__:
    resolve()
