import sys


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

    L = []

    for i in range(X):
        s =K//(i+1)
        for j in range(min(Y, s + 1)):
            t =A[i] +B[j]
            for k in range(min(Z, s // (j + 1) + 1)):
                L.append(t + C[k])

    L.sort(reverse=True)

    for i in range(K):
        print(L[i])


if __name__ == "__main__":
    main()
