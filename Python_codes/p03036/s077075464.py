def resolve():
    r, D, x = map(int, input().split())

    ans = [0 for _ in range(11)]
    ans[0] = x
    for i in range(1, 11):
        ans[i] = r * ans[i-1] - D

    print('\n'.join(map(str, ans[1:])))


resolve()