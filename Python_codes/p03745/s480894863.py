N = int(input())
A = [int(i) for i in input().split()]

if N == 1:
    print(1)
else:
    pre = A[0]
    flg = 0
    ans = 1
    for i in range(1, N):
        now = A[i]
        diff = now - pre
        if flg == 1:
            if diff >= 0:
                pass
            else:
                ans += 1
                flg = 0
        elif flg == -1:
            if diff <= 0:
                pass
            else:
                ans += 1
                flg = 0
        else:
            if diff > 0:
                flg = 1
            elif diff < 0:
                flg = -1
            else:
                pass
        pre = now
        # print("i: {}, A[i]: {}, flg: {}, ans:{}".format(i, A[i], flg, ans))
    print(ans)
