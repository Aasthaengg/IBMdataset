#!/usr/bin/env python3


def main():
    A, B, C = [int(ele) for ele in input().split()]
    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif C == A:
        print(B)


if __name__ == "__main__":
    main()
