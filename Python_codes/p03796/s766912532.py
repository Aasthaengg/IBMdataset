def factorial(x, mod=10**9+7):
    # x!
    # 階乗
    # ex) factorial(5) = 120
    tmp = 1
    for i in range(1, x+1):
        tmp = (tmp * i) % mod
    return tmp

a=int(input())
print(factorial(a))
