import sys
from string import ascii_lowercase as AL

input = sys.stdin.readline


def main():
    S = input().rstrip()
    K = int(input())

    N = len(S)
    T = [s for s in S]
    for i in range(N):
        if T[i] == "a":
            continue
        idx = AL.index(T[i])
        if 26 - idx <= K:
            K -= (26 - idx)
            T[i] = "a"

    _, r = divmod(K, 26)
    T[-1] = AL[AL.index(T[-1]) + r]

    ans = "".join(T)
    print(ans)


if __name__ == "__main__":
    main()
