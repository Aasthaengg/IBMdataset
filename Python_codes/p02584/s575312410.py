# coding=utf-8

if __name__ == '__main__':
    X, K, D = map(int, input().split())

    ABS_X = abs(X)

    if K * D <= ABS_X:
        ans = ABS_X - (K * D)

    else:
        r = ABS_X // D
        l = ABS_X // D + 1
        if r % 2 == K % 2:
            ans = abs(ABS_X - D * r)
        else:
            ans = abs(ABS_X - D * l)

    print(ans)

