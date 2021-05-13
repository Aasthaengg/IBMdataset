def resolve():
    a, b, x = list(map(int, input().split()))
    result = b // x - (a - 1) // x
    print(result)

resolve()