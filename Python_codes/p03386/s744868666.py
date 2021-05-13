def actual(A, B, K):
    min_a = A
    max_a = min(A + (K - 1), B)

    min_b = max(B - (K - 1), max_a + 1)
    max_b = B

    left = list(range(min_a, max_a + 1))
    right = list(range(min_b, max_b + 1))

    return '\n'.join(map(str, sorted(set(left + right))))

  
A, B, K = map(int, input().split())
print(actual(A, B, K))