import numpy as np

N, K = map(int, input().split())
A = np.array(input().split(), dtype=np.int64)

digits = len(format(K, "b"))
bits_list = [((A >> shift) & 1).sum() for shift in range(digits)]
bits_list.reverse()

X = 0
half = (N + 1) // 2
digit = 1 << (len(format(K, "b")) - 1)

for bits in bits_list:
    if bits < half and (X | digit) <= K:
        A ^= digit
        X |= digit
    digit >>= 1

print(A.sum())
