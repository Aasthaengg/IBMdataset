k, a, b = map(int, input().split())
k += 1

if a + 3 <= b:
    x = 0
    k -= (a+2)
    x += b

    n, res = divmod(k, 2)
    x += (b-a)*n+res
    print(x)
else:
    print(k)