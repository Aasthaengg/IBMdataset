# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from heapq import heappop, heappush
import sys
def main(X, Y, Z, K, A, B, C):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    used = set()
    q = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
    used.add((0, 0, 0))
    for i in range(K):
        v, ai, bi, ci = heappop(q)
        print(-v)
        for nai, nbi, nci in [(ai + 1, bi, ci), (ai, bi + 1, ci), (ai, bi, ci + 1)]:
            if nai >= X or nbi >= Y or nci >= Z: continue
            if (nai, nbi, nci) in used: continue
            used.add((nai, nbi, nci))
            heappush(q, (-(A[nai] + B[nbi] + C[nci]), nai, nbi, nci))

if __name__ == '__main__':
    input = sys.stdin.readline
    X, Y, Z, K = map(int, input().split())
    *A, = map(int, input().split())
    *B, = map(int, input().split())
    *C, = map(int, input().split())
    main(X, Y, Z, K, A, B, C)
