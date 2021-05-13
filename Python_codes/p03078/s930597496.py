# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from itertools import product
import sys
def main(X, Y, Z, K, A, B, C):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for x in range(1, X + 1):
        if x > K: break
        for y in range(1, Y + 1):
            if x * y > K: break
            for z in range(1, Z + 1):
                if x * y * z > K: break
                ans.append(A[x - 1] + B[y - 1] + C[z - 1])
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

if __name__ == '__main__':
    input = sys.stdin.readline
    X, Y, Z, K = map(int, input().split())
    *A, = map(int, input().split())
    *B, = map(int, input().split())
    *C, = map(int, input().split())
    main(X, Y, Z, K, A, B, C)
