N = int(input())
ans = 0
n = 1
while n*n < N:
    if not N % n and n*(n+1) != N:
        ans += N//n-1
    n += 1
print(ans)
