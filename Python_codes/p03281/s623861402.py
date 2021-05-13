N = int(input())

def divisor(n):
    res = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            res.append(i)
            if i != n//i:
                res.append(n // i)
        i += 1
    return res

ans = 0
for i in range(1, N+1, 2):
    res = len(divisor(i))

    ans += 1 if res == 8 else 0

print(ans)
