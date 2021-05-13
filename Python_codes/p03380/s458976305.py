def d_binomial_coefficients():
    N = int(input())
    A = sorted([int(i) for i in input().split()])  # ソートしておく

    n = A[-1]  # n を大きく、r を n/2 に近づけると comb(n, r) は大きい
    r = min(A[:-1], key=lambda x: abs(n / 2 - x))
    return f'{n} {r}'

print(d_binomial_coefficients())