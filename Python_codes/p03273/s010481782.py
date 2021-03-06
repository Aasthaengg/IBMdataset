import numpy as np

def main():

    H,W = map(int,input().split())
    A = [[0 if s == "." else 1 for s in list(input())] for _ in range(H)]

    for i in reversed(range(H)):
        if sum(A[i]) == 0:
            A.pop(i)

    A = np.array(A).T.tolist()
    for i in reversed(range(W)):
        if sum(A[i]) == 0:
            A.pop(i)
    A = np.array(A).T.tolist()

    for i in range(len(A)):
        print("".join(["." if i == 0 else "#" for i in A[i]]))

main()
