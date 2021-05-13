a, b, x = map(int, input().split())


def n_div(a):
    # n of divisor <= a
    return a // x


answer = n_div(b) - n_div(a - 1)
print(answer)
