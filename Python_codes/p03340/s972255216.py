#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    right = 1
    xor = A[0]
    sum = A[0]
    ans = 0
    for left in range(N):
        while right < N and xor ^ A[right] == sum + A[right]:
            xor ^= A[right]
            sum += A[right]
            right += 1

        ans += right - left

        if left == right:
            right += 1

        xor ^=A[left]
        sum -=A[left]
    print(ans)
    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
