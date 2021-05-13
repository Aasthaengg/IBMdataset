def actual(N):
    a, b = divmod(N, 10)

    if a == 9 or b == 9:
        return 'Yes'

    return 'No'

N = int(input())
print(actual(N))