x,k,d = map(int,input().split())
x = abs(x)
r = x % d
q = x // d
if (k*d) < x:
    print(x - (k*d))
else:
    if (k - q) % 2 == 0:
        print(r)
    else:
        print(abs(d-r))