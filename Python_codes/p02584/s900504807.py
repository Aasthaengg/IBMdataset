x, k, d = map(int, input().split())
x = abs(x)

if x - k*d > 0:
    print(x-k*d)
else:
    v = x // d
    k -= v
    x = x - d*v
    if k % 2 == 0:
        print(x)
    else:
        print(min(abs(x-d), abs(x+d)))