def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i, b in enumerate(B):
        if A[i] <= b:
            ans += A[i]
            remain = b - A[i]
        else:
            ans += b
            remain = 0
        if remain > 0:
            if A[i+1] < remain:
                ans += A[i+1]
                A[i+1] = 0
            else:
                ans += remain
                A[i+1] -= remain
    print(ans)


if __name__ == '__main__':
    main()
