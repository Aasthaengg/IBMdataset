x, k, d = map(int, input().split())

x = abs(x)

if x>k*d:
    print(x-k*d)
else:
    a = x//d
    if (k-a)%2==0:
        print(x-a*d)
    else:
        print(abs(x-a*d-d))
