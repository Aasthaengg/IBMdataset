import sys
# from collections import defaultdict
# from collections import Counter
# from queue import Queue
# sys.setrecursionlimit(2000000)

import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

MOD = 1000000007

def main():
    # N = int(input())

    N, K = [int(s) for s in input().split()]

    # sum of 0~i
    s = 0
    comm_sum = [0]
    for i in range(1, N+1):
        s += i
        comm_sum.append(s)

    # sys.stderr.write('{}\n'.format(comm_sum))

    ans = 0
    for k in range(K, N+1 + 1):
        if k == N + 1:
            ans = (ans + 1) % MOD
            continue
        max_a = comm_sum[N] - comm_sum[N - k]
        min_a = comm_sum[k - 1]
        diff = max_a - min_a + 1
        ans = (ans + diff) % MOD
        # sys.stderr.write('k = {}\n'.format(k))
        # sys.stderr.write('{}\n'.format(min_a))
        # sys.stderr.write('{}\n'.format(max_a))
        # sys.stderr.write('{}\n'.format(diff))
        # sys.stderr.write('--\n')

    print(ans)

    return 0

if __name__ == '__main__':
    sys.exit(main())
