import sys

H, W, A, B = map(int, sys.stdin.readline().split())

for i in range(H):
    for j in range(W):
        if i < B:
            if j < A:
                print(0, end="")
            else:
                print(1, end="")
        else:
            if j < A:
                print(1, end="")
            else:
                print(0, end="")
    print("")