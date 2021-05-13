def codefes16q_b():
    _, _ = map(int, input().split())
    A = list(sorted(map(int, input().split())))
    x = 2 * A[-1] - sum(A)
    ans = max(x-1, 0)
    print(ans)

codefes16q_b()