import sys
from collections import Counter

input = sys.stdin.readline


def main():
    K, T = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    prev_j = -1
    for i in range(K):
        j_max = 0
        n_max = 0
        for j in range(T):
            if j == prev_j:
                continue
            if a[j] > n_max:
                n_max = a[j]
                j_max = j
        if n_max == 0:
            ans += 1
        else:
            prev_j = j_max
            a[j_max] -= 1
    print(ans)


if __name__ == "__main__":
    main()
