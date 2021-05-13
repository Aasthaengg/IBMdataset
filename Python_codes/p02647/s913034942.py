def main():
    import sys
    input = sys.stdin.readline
    N, K = [int(x) for x in input().strip().split()]
    A = [int(x) for x in input().strip().split()]
    l = [0] * (N + 1)
    for i, a in enumerate(A):
        l[max(0, i-a)] += 1
        l[min(N, i+a+1)] -= 1
    p = 0
    cumsum = [0] * (N + 1)
    for i in range(N+1):
        p += l[i]
        cumsum[i] = p
    cumsum_ = A + [0]
    for k in range(min(K-1, 50)):
        p = 0
        for i in range(N+1):
            l[max(0, i-cumsum[i])] += 1
            l[min(N, i+cumsum[i]+1)] -= 1
            l[max(0, i-cumsum_[i])] -= 1
            l[min(N, i+cumsum_[i]+1)] += 1

        cumsum_ = cumsum[:]
        for i in range(N+1):
            p += l[i]
            cumsum[i] = p

    print(*cumsum[:-1])

if __name__ == '__main__':
    main()