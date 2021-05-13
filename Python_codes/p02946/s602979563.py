def actual(k, x):
    n_min = x - (k - 1)
    n_max = x + (k - 1)

    return ' '.join([str(i) for i in range(n_min, n_max + 1)])

k, x = map(int, input().split())
print(actual(k, x))