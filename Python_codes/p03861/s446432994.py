def count_muls(num, x):
    if num < 0:
        return 0
    return num // x + 1

def resolve():
    a, b, x = map(int, input().split())
    print(count_muls(b, x) - count_muls(a-1, x))

resolve()