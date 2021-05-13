import numpy as np


def main():
    n = int(input())
    while True:
        if int(np.sqrt(n)) == np.sqrt(n):
            print(n)
            exit()
        else:
            n = n-1


if __name__ == "__main__":
    main()
