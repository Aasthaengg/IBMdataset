def coins(probabilities):
    n = len(probabilities)
    res = [0] * (n + 1)
    res[0] = 1

    for i, p in enumerate(probabilities, start=1):
        q = 1 - p
        carry = 0
        for j in range(i + 1):
            res[j], carry = res[j] * q + carry, res[j] * p

    return sum(res[(n + 1) // 2:])


def main():
    input()  # n
    probabilities = [float(x) for x in input().split()]
    return coins(probabilities)


print(main())
