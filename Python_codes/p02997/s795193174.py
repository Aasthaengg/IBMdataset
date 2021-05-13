def main():
    N, K = (int(i) for i in input().split())
    if (N-1)*(N-2)//2 < K:
        return print(-1)
    need_reduce = (N-1)*(N-2)//2 - K
    M = (N-1) + need_reduce
    ans = [[1, j] for j in range(2, N+1)]
    i = 2
    while need_reduce > 0:
        j = i+1
        while j <= N and need_reduce > 0:
            ans.append([i, j])
            j += 1
            need_reduce -= 1
        i += 1
    print(M)
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
