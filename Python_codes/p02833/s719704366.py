N = int(input())

k = 10
ans = 0
if N % 2 != 0:
    ans = 0
else:
    while k <= N:
        ans += N // k
        k *= 5

print(ans)