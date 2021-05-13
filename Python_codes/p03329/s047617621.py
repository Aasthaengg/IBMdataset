n = int(input())
# n < 100000
res = n

for i in range(n+1):
    c = 0
    t = i
    while t > 0:
        c += t % 6
        t //= 6
    t = n - i
    while t > 0:
        c += t % 9
        t //= 9
    if res > c:
        res = c

print(res)
