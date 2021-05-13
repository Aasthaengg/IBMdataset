import numpy as np
import numba
import math

@numba.njit
def main(N, K, steps):

    dpt = [10**9] * (N)
    dpt[0] = 0

    for i in range(N):
        for j in range(1, K+1):
            if i + j > N - 1:
                break
            ij = i + j
            x = dpt[i] + abs(steps[i] - steps[ij])
            if x < dpt[ij]:
                dpt[ij] = x

    print(dpt[N-1])

if __name__ == "__main__":
    N, K = map(int, input().split())
    steps = np.array(list(map(int, input().split())), dtype=np.int32)
    main(N, K, steps)
