def resolve():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    A = sorted(a)
    count = 0
    ans = 0
    for i in A:
        if count < x:
            count += i
            ans += 1
    if count > x:
        ans -= 1
    if sum(A) < x:
        ans -= 1
    print(ans)
resolve()