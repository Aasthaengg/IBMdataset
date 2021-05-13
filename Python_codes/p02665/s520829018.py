def main():
    N = int(input())
    A = list(map(int, input().split()))
    # verification
    x = 1
    mx = [0] * (N+1)
    for i, a in enumerate(A):
        if i != N and x <= a:
            print(-1)
            return
        if i == N and x < a:
            print(-1)
            return
        x -= a
        mx[i] = x
        x *= 2
    ans = 0
    edge = 0
    for i in range(N+1)[::-1]:
        a = A[i]
        edge = min(edge, mx[i])
        ans += edge + a
        edge += a
    print(ans)


if __name__ == "__main__":
    main()
