N, K = map(int, input().split())

if K % 2 == 1:
    tmp = N // K
    ans = tmp ** 3
    print (ans)

else:
    tmp = N // K
    ans = tmp ** 3

    tmp = N // (K // 2) - tmp
    ans += tmp ** 3

    print (ans)
