def solve():
    N = int(input())
    M = 0
    Ans = []
    if N % 2 == 0:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N + 1:
                    Ans.append([i, j])
                    M += 1
    else:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N:
                    Ans.append([i, j])
                    M += 1
    print(M)
    for i, j in Ans:
        print(i, j)


    return 0

if __name__ =="__main__":
    solve()