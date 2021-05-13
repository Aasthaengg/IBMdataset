def caddi18b_b():
    N, H, W = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    for a, b in P:
        if H <= a and W <= b: ans += 1
    print(ans)

caddi18b_b()