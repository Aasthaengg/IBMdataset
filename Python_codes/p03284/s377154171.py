def actual(n, k):
    if n % k == 0:
        return 0

    return 1

n, k = map(int, input().split())
print(actual(n, k))