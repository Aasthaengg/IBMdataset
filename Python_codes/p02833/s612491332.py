N = int(input())
if N%2:
    print(0)
else:
    ans = 0
    N //= 2
    while N:
        N //= 5
        ans += N
    print(ans)
