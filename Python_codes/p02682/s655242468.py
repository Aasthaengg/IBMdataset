A, B, C, K = map(int, input().split())

ans = 0
if A >= K:
    print(K)
    exit()
else:
    ans += A
    K -= A
    if B >= K:
        print(ans)
        exit()
    else:
        K -= B
        ans -= K
        print(ans)
