N = int(input())
ans = 10000

for x in range(1, N // 2 + 1):
    SUM = 0
    A = x
    B = N - x
    while A > 0 or B > 0:
        SUM += A % 10 + B % 10
        A //= 10
        B //= 10
    if ans > SUM:
        ans = SUM

print(ans)