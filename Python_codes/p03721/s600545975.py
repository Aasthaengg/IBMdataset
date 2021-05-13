import numpy as np


def main():
    n, k = map(int, input().split())
    Counts = [0] * (10**5 + 1)
    for _ in range(n):
        a, b = map(int, input().split())
        Counts[a] += b
    cumsum = np.cumsum(Counts)
    for i in range(10**5+1):
        if cumsum[i] >= k:
            ans = i
            break
    print(ans)


if __name__ == "__main__":
    main()
