#!/usr/bin/env python3
def main():
    def solve(n):
        if n == 1:
            return 1
        return solve(n // 2) * 2 + 1

    H = int(input())

    print(solve(H))


if __name__ == '__main__':
    main()
