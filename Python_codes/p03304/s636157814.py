n, m, d = map(int, input().split())

if d == 0:
    tmp = n
elif d >= n:
    tmp = 0
else:
    tmp = (n-d)*2

print((tmp/n**2)*(m-1))
