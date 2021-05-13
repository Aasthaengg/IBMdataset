N = int(input())
if N % 10 == 0:
    ans = 10
else:
    ans = 0
    while N > 0:
        ans += N % 10
        N //= 10
print(ans)