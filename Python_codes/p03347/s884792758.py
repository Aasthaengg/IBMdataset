def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    if A[0] > 0:
        print(-1)
        return
    for n in range(N - 1):
        if  A[n + 1] >= A[n] + 2:
            print(-1)
            return
    # 後ろから見ていく。前項以上なら加算、前項未満なら加算せず。
    A = A[::-1]
    ans = A[0]
    for n in range(N - 1):
        if A[n + 1] >= A[n]:
            ans += A[n + 1]
    print(ans)


if __name__ == '__main__':
    main()