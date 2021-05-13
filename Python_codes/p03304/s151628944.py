n, m, d = input().split()
n = int(n)
m = int(m)
d = int(d)

if d == 0:
    x = n
    if n == 1:
        result = m - 1
    else:
        result = x*(m-1)/n**2


else:
    x = 2*(n - d)

    result = x*(m-1)/n**2

print(result)