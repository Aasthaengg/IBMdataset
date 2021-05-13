def main():
    import sys
    import heapq
    from copy import deepcopy
    from collections import deque
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    N, K = [int(x) for x in input().strip().split()]
    V = [int(x) for x in input().strip().split()]
    ans = -float('inf')
    for l in range(min(N, K)+1):
        for r in range(min(N, K)-l+1):
            vt = sorted(V[:l] + V[N-r:])
            c = 0
            i = 0
            for i in range(len(vt)):
                if c == (K-l-r):
                    break
                if vt[i] < 0:
                    vt[i] = 0
                    c += 1
                else:
                    break
            ans = max(ans, sum(vt))

    print(ans)

if __name__ == '__main__':
    main()