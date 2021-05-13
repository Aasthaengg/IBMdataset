n = int(input()) - 1 # n=n-1
c, x = 0, 1
while x*x <= n:
    c += (n//x - x)*2 + 1
    x += 1
print(c)
