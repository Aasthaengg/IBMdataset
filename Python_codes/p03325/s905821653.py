def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    i = 0
    ans = 0
    while i<n:
        if A[i] % 2 == 0:
            A[i] //= 2
            ans += 1
        else:
            i += 1
    print(ans)
resolve()