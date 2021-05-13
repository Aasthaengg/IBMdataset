def actual(n):
    if 1 <= n <= 999:
        return 'ABC'

    return 'ABD'

n = int(input())
print(actual(n))