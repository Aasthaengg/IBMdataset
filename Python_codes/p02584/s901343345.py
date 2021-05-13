n, k, d = map(int,input().split())
if abs(n) - k * d < 0:
    j = abs(n)//d
    z = k - j
    if z % 2 == 0:
        print(abs(n)-j*d)
    else:
        print(d-(abs(n)-j*d))
else:
    print(abs(n) - k * d)