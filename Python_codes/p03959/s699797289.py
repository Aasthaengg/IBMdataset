def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    fixed_t = [0] * N
    max_t = 0
    for i in range(N):
        t = T[i]
        if t > max_t:
            fixed_t[i] = 1
        max_t = max(max_t, t)
    fixed_a = [0] * N
    max_a = 0
    for i in range(N - 1, -1, -1):
        a = A[i]
        if a > max_a:
            fixed_a[i] = 1
        max_a = max(max_a, a)
    ans = 1
    for i in range(N):
        if fixed_t[i] == fixed_a[i] == 1:
            if T[i] != A[i]:
                print(0)
                return
        elif fixed_t[i] == 0 and fixed_a[i] == 1:
            if T[i] < A[i]:
                print(0)
                return
        elif fixed_t[i] == 1 and fixed_a[i] == 0:
            if T[i] > A[i]:
                print(0)
                return
        else:
            ans *= min(A[i], T[i])
            ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()