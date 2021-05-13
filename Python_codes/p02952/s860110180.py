def resolve():
    N = input()
    n = len(N)
    ans = 0
    if n % 2 == 0:
        for i in range(1, n):
            if i % 2 == 1:
                ans += 9*(10**(i-1))
        print(ans)
    else:
        for i in range(1, n-1):
            if i % 2 == 1:
                ans += 9*(10**(i-1))
        print(ans + int(N) + 1 - 10**(n-1))
resolve()