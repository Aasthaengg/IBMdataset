import numpy as np


def main():
    x = int(input())
    A = np.arange(-120, 120)
    a = A ** 5
    for i, a_1 in enumerate(a):
        for j, a_2 in enumerate(a):
            if a_1 - a_2 == x:
                print(A[i], A[j])
                return


if __name__ == "__main__":
    main()
