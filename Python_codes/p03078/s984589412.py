# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from itertools import product
import sys
def main(X, Y, Z, K, A, B, C):
    AB = sorted([a + b for a, b in product(A, B)], reverse=True)
    ABC = sorted([ab + c for ab, c in product(AB[:K], C)], reverse=True)
    for k in range(K):
        print(ABC[k])

if __name__ == '__main__':
    input = sys.stdin.readline
    X, Y, Z, K = map(int, input().split())
    *A, = map(int, input().split())
    *B, = map(int, input().split())
    *C, = map(int, input().split())
    main(X, Y, Z, K, A, B, C)
