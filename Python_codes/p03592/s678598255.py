def main():
    N, M, K = list(map(int, input().split()))
    ans = False
    for i in range(N+1):
        for j in range(M+1):
            x = i * M + j * N - (i * j) * 2
            # print(i, j, x)
            if x == K:
               ans = True 
    if ans:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()