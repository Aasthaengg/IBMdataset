a, b, k = map(int, input().split())

if a >= k:
    print(a-k, b)
else:
    k -= a
    if b >= k:
        print(0, b-k)
    else:
        print(0, 0)