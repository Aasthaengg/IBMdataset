n = int(input())
a = list(map(int, input().split()))


def calc(val):
    # valには、１か−１を入れる。
    if (val * a[0] > 0):
        # 狙った符号のパターン
        temp = a[0]
        ans01 = 0

    else:
        # 違うパターン
        add = abs(a[0]) + 1
        ans01 = add
        temp = val

    for i in range(1, n):
        tar = temp + a[i]
        if (tar * temp < 0):
            temp = tar
        else:
            add = abs(tar) + 1
            ans01 += add
            if (temp > 0):
                temp = -1
            else:
                temp = 1

    return ans01


ans = min(calc(1), calc(-1))


print(ans)
