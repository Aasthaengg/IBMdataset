#!/usr/bin/env python3
def main():
    K, N = map(int, input().split())
    A = [int(x) for x in input().split()]

    max_length = A[0] + K - A[-1]
    for i in range(1, len(A)):
        max_length = max(max_length, A[i] - A[i - 1])
    print(K - max_length)


if __name__ == '__main__':
    main()
