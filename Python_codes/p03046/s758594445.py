import sys
input = sys.stdin.readline
from functools import reduce
from operator import xor


def read():
    M, K = map(int, input().strip().split())
    return M, K


def solve(M, K):
    seq = [str(0) for i in range(2**(M+1))]
    if K == 0:
        for i in range(2**M):
            seq[2*i] = str(i)
            seq[2*i+1] = str(i)
    else:
        if K >= 2**M:
            return -1
        # (A) K ... 0 K 0 rev(...), xor(...) == K の形を作れればOK
        S = [a for a in range(2**M) if a not in (0, K)]
        if len(S) == 0 or reduce(xor, S) != K:
            return -1
            
        j = 0
        for i in range(2**M-2):
            j += 1
            if j == K:
                j += 1
            seq[i+1] = str(j)
            seq[2**(M+1) - i - 1] = str(j)
        seq[0] = str(K)
        seq[2**M] = str(K)
        
    return " ".join(seq)


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
