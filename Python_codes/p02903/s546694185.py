import numpy as np


def main():
    H, W, A, B = map(int, input().split())
    s = np.zeros((H, W), dtype=np.int64)
    s[:B, :A] = 1
    s[B:, A:] = 1
    
    for l in s:
        print(*l, sep='')


if __name__ == "__main__":
    main()