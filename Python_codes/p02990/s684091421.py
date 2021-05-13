from scipy.misc import comb
n, k = map(int, input().split())
for i in range(1, k + 1):
    print(int(comb(n - k + 1, i, exact=True)) * comb(k - 1, i - 1, exact=True) % (pow(10, 9) + 7))