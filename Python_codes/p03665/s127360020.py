from scipy.special import comb
import numpy as np

N, P = map(int, input().split())
A = np.array(list(map(int, input().split())))

A = A % 2 != 0
odd = np.sum(A)
even = N - odd
# print(A, odd, even)

ans = 0
odd_num = 0
even_num = 0
if P == 1:
    for i in range(1, odd + 1, 2):
        odd_num += comb(odd, i, exact=True)
    even_num = pow(2, even)
    ans = odd_num * even_num
else:
    for i in range(0, odd + 1, 2):
        odd_num += comb(odd, i, exact=True)
    even_num = pow(2, even)
    ans = odd_num * even_num
    # print(odd_num, even_num)
print(ans)
