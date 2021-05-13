import numpy as np


def main():
    n = int(input())
    abcde = [int(input()) for _ in range(5)]
    min_abcde = min(abcde)
    ans = int(np.ceil(n/min_abcde) + 4)
    print(ans)


if __name__ == "__main__":
    main()
