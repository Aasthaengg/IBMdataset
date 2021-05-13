x,k,d = map(int, input().split())
x = abs(x)
kd = k*d

if kd<=x:
    print(x-kd)
else:
    count = x // d
    k_dash = k - count
    x -= count * d
    if k_dash % 2 == 0:
        print(x)
    else:
        print(d-x)
