def fact(n):
    val = 1
    for i in range(2, n + 1):
        val *= i
        val %= 10**9 + 7
    return val

x, y = map(int,input().split())
ans = 1

if abs(x-y) > 1:
    print(0)

elif x == y:
    print((fact(x)**2 *2) % (10**9+7))

else:
    print((fact(x) * fact(y)) % (10**9+7))
