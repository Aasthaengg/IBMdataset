def resolve():
    A, B = list(map(int, input().split()))
    if B == 1:
        ans = 0
        print(ans)
        return
    cnt = A
    ans = 1
    while cnt < B:
        cnt += A-1
        ans += 1

    print(ans)

if '__main__' == __name__:
    resolve()