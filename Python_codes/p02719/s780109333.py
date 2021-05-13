def abc161c_replacing_integer():
    n, k = map(int, input().split())
    val = n // k
    result = min(n - val * k, abs(n - (val+1) * k))
    print(result)

abc161c_replacing_integer()