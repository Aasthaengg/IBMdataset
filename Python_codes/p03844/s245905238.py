import sys

input = sys.stdin.readline


def main():
    S = input().split()
    A = int(S[0])
    op = S[1]
    B = int(S[2])
    if op == "+":
        print(A + B)
    else:
        print(A - B)


if __name__ == "__main__":
    main()
