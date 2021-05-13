def actual(k):
    n_even = k // 2
    n_odd = (k + 1) // 2

    return n_even * n_odd

k = int(input())
print(actual(k))
