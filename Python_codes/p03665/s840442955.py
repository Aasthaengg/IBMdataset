import functools


@functools.lru_cache(maxsize=None)
def num_counts(size, P):
    if size == 1:
        return 1 + (A[size - 1] + 1) % 2 if P == 0 else A[size - 1] % 2
    if A[size - 1] % 2 == 0:
        return num_counts(size - 1, P) * 2
    else:
        return num_counts(size - 1, P) + num_counts(size - 1, (P + 1) % 2)


if __name__ == "__main__":
    N, P = [int(x) for x in input().split(" ")]
    A = [int(x) for x in input().split(" ")]
    print(num_counts(len(A), P))
