n, m, d = map(int, input().split())

if n%2 == 0:
    if d >= n//2 or d == 0:
        p = n
    else:
        p = 2*d + 2*((n-d)-d)
else:
    if d >= -(-n//2) or d == 0:
        p = n
    elif d == n//2:
        p = 2*d + 2
    else:
        p = 2*d + 2*((n-d)-d)

p /= n**2

print((m-1) * p)