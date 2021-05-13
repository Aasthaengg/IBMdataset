def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if A[0] > x:
        ans += A[0] - x
        A[0] = x

    for i in range(n - 1):
        j = i + 1
        if j < n and A[i] + A[j] > x:
            diff = A[i] + A[j] - x
            ans += diff
            A[j] -= diff
    print(ans)


if __name__ == '__main__':
    main()