def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    ans = 0
    pre = 0
    for a in A[::-1]:
        if a >= pre:
            ans += a
        elif a+2 <= pre:
            return print(-1)
        pre = a
    if A[0] != 0:
        return print(-1)
    print(ans)


if __name__ == '__main__':
    main()
