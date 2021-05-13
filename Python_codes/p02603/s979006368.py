def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans, b = 1000, 0
    def buy(a):
        nonlocal b, ans
        b += ans // a
        ans %= a
    def sell(a):
        nonlocal b, ans
        ans += b * a
        b = 0
    if A[0] < A[1]: buy(A[0])
    for i in range(1, n - 1):
        if A[i - 1] >= A[i] < A[i + 1]:
            buy(A[i])
        elif A[i - 1] <= A[i] > A[i + 1]:
            sell(A[i])
        else:
            continue
    if b > 0:
        sell(A[-1])
    print(ans)

if __name__ == '__main__':
    main()
