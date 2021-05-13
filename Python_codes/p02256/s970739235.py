def gcd(x,y):
    while 1:
        tmp = x%y
        if tmp==0:
            return y
        x = y
        y = tmp

a = list(map(int, input().split()))

if a[0]<=a[1]:
    s = gcd(a[1],a[0])
else:
    s = gcd(a[0],a[1])

print(s)
