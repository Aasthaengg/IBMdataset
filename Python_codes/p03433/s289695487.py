def actual(amount, n_1yen):
    fraction = amount % 500

    if fraction <= n_1yen:
        return 'Yes'
    else:
        return 'No'


N = int(input())
A = int(input())

print(actual(N, A))
