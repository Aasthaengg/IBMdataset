N, K, S = map(int, input().split())
if K == N:
    print(*([S] * N), sep = ' ')
elif S == 1:
    print(*([1] * K + [10 ** 9] * (N-K)), sep = ' ')
else:
    half2 = S // 2
    half1 = S - half2
    ans = [half1, half2] * (K // 2)
    ans += [half1]
    if K % 2:
        ans += [half2]
    rem = 1 if S == 10 ** 9 else 10 ** 9
    ans += [rem] * (N - len(ans))

    print(*ans, sep = ' ')