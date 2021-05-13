def actual(A, B, K):
    min_left = A
    max_left = min(A + (K - 1), B)

    min_right = max(B - (K - 1), max_left + 1)
    max_right = B

    left = set(range(min_left, max_left + 1))
    right = set(range(min_right, max_right + 1))

    unique_nums = left | right

    return '\n'.join(map(str, sorted(unique_nums)))

A, B, K = map(int, input().split())
print(actual(A, B, K))