N,A,B = map(int,input().split())

ans =0

while N > 0:
    n = N
    t = 0

    while n > 0:
        t += n % 10
        n //= 10

    if A <= t <= B:
        ans += N

    N -= 1

print(ans)