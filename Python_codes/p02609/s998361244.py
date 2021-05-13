def f(n):
    ret = 1
    while n > 0:
        n %= bin(n).count('1')
        ret += 1
    return ret

if __name__ == "__main__":
    n = int(input())
    x = input()
    cnt = x.count('1')

    if cnt == 1:
        for k in x[:-1]:
            if k == '0':
                print(1)
            else:
                print(0)
        if x[-1] == '1':
            print(0)
        else:
            print(2)
        exit()

    xNum = 0
    for k in x:
        xNum <<= 1
        if k == '1':
            xNum += 1
    ans = []
    p = xNum % (cnt + 1)
    m = xNum % (cnt - 1)

    for i in range(n):
        if x[i] == '0':
            ans.append(f((p + pow(2, n - i - 1, cnt + 1)) % (cnt + 1)))
        else:
            ans.append(f((m - pow(2, n - i - 1, cnt - 1)) % (cnt - 1)))
    print(*ans, sep='\n')
