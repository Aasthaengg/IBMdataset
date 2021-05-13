def resolve():
    S = str(input())
    ans = 2 * min(S.count('1'), S.count('0'))

    print(ans)
    return
resolve()