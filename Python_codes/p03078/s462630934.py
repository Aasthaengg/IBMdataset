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

    L=[]

    for i in range(X):
        for j in range(Y):
            for k in range(X):
                if (i+1)*(j+1)*(k+1)<=K:
                    L.append(A[i]+B[j]+C[k])
                else:
                    break

    L.sort(reverse=True)

    for i in range(K):
        print(L[i])



if __name__ == "__main__":
    main()
