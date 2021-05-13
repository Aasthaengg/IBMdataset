def main():
    N, K = map(int, input().split())
    if (N -1) * (N - 2) / 2 < K:
        print(-1)
        return -1
    l = [(1, i) for i in range(2,N+1)]
    i = 2
    j = 3
    for _ in range(int((N-1) * (N-2)/2) - K):
        l.append((i,j))
        if j == N:
            i += 1
            j = i + 1
        else:
            j += 1
    print(len(l))
    for i, j in l:
        print(i, j)
main()
