n, m, d = map(int, input().split())

if d > 0:
    pair = 2 * d + 2 * (n - 2 * d)
elif d == 0:
    pair = n
prob = pair/(n**2)
print((m-1)*prob)