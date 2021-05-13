import sys
 
import numba as nb
import numpy as np
 
input = sys.stdin.readline
 
 
@nb.njit("i8[:](i8,i8,i8[:])", cache=True)
def solve(N, K, A):
    for _ in range(min(41, K)):
        A_cumsum = np.zeros(shape=N, dtype=np.int64)
        for i in range(N):
            A_cumsum[max(0, i - A[i])] += 1
            b = i + A[i] + 1
            if N - 1 < b:
                pass
            else:
                A_cumsum[b] -= 1
        A = np.cumsum(A_cumsum)
    return A
 
 
def main():
    N, K = map(int, input().split())
    A = np.array(input().split(), dtype=np.int64)
 
    ans = solve(N, K, A)
 
    print(" ".join(map(str, ans)))
 
 
if __name__ == "__main__":
    main()