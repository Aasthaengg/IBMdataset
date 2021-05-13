import sys
import heapq


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    a = 0
    b = 0
    c = 0
    k = 1

    L = []

    for i in range(X):
        for j in range(Y):
            L.append(A[i] + B[j])

    L.sort(reverse=True)
    newL = L[:min(3000, X * Y)]
    XY = len(newL)
    L=[]
    for i in range(XY):
        for j in range(Z):
            L.append(newL[i]+C[j])

    L.sort(reverse=True)

    for j in range(K):
        print(L[j])



if __name__ == "__main__":
    main()
