#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()

    res = 0
    R, G, B = S.count('R'), S.count('G'), S.count('B')
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            k = j + j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                res += 1
    print(R * G * B - res)


if __name__ == '__main__':
    main()
