import itertools


def actual(N, K):
    op_A = lambda i: i * 2
    op_B = lambda i: i + K

    patterns = list(itertools.product((op_A, op_B), repeat=N))

    results = []

    for pattern in patterns:
        num = 1

        for op in pattern:
            num = op(num)

        results.append(num)

    return min(results)

N = int(input())
K = int(input())

print(actual(N, K))
