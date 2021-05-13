def factors(n):
    d, res = 1, 0
    while d*d <= n:
        if n % d == 0:
            if d*d == n:
                res += 1
            else:
                res += 2
        d += 1
    return res


N = int(input())

ans = 0
for i in range(1,N+1,2):
    if factors(i) == 8:
        ans += 1

print(ans)