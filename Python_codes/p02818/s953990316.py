a, b, k = map(int, input().split())

if a >= k:
    a -= k
    print(a, b)
else:
    if b >= k-a:
        b -= k-a
        print(0, b)
    else:
        print(0, 0)