def resolve():
    N = int(input())
    power = 1
    for i in range(1, N+1):
        power *= i
        power = power%(10**9+7)
    print(power)


if '__main__' == __name__:
    resolve()