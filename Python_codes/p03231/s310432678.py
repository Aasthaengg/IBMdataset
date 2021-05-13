import math
def main4():
    N, M = map(int, input().split())
    S = input()
    T = input()

    L = (N * M) // math.gcd(N, M)

    pair = dict()

    for i in range(1, N + 1):
        idx = (i - 1) * (L // N) + 1
        pair[idx] = S[i - 1]

    for i in range(1, M + 1):
        idx = (i - 1) * (L // M) + 1

        if idx in pair.keys():
            if pair[idx] != T[i - 1]:
                print(-1)
                exit()

    print(L)

if __name__ == "__main__":
    main4()