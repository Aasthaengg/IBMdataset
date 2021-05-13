def resolve():
    X = int(input())
    res = (X // 11) * 2
    rem = X % 11
    if rem != 0:
        if rem <= 6:
            res += 1
        else:
            res += 2
    print(res)

if '__main__' == __name__:
    resolve()