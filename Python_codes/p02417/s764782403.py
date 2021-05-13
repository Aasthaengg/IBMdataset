#
# 8c
#
import sys


def main():
    A = "abcdefghijklmnopqrstuvwxyz"
    r = [0 for _ in range(26)]
    S = sys.stdin.read()

    for i in range(len(S)):
        for j in range(len(A)):
            if S[i].lower() == A[j]:
                r[j] += 1
                break
    for i in range(26):
        print(f"{A[i]} : {r[i]}")


if __name__ == '__main__':
    main()

