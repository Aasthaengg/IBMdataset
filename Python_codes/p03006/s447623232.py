def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for j in range(N)]
    if N == 1:
        return print(1)
    A.sort()
    from collections import defaultdict
    cnt = defaultdict(int)
    for i in range(N):
        for j in range(i+1, N):
            # print(A[i], A[j], (A[j][0] - A[i][0], A[j][1] - A[i][1]))
            cnt[(A[j][0] - A[i][0], A[j][1] - A[i][1])] += 1
    # print(cnt.values())
    ans = (N-1) - (sorted(cnt.values())[-1] - 1)
    print(ans)


if __name__ == '__main__':
    main()
