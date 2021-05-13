def resolve():
    A, B = list(map(int, input().split()))
    num = list(range(A, B+1))
    ans = 0
    for n in num:
        if str(n) == str(n)[::-1]:
            ans += 1
    print(ans)
    return

resolve()