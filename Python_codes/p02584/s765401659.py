x, k, d = map(int, input().split())

if abs(x) >= d * k:
    print(abs(x) - d * k)
else:
    if (k - abs(x)//d) % 2 == 0:
        print(abs(x) - d * (abs(x)//d))
    else:
        print(abs(abs(x) - d * (abs(x)//d + 1)))