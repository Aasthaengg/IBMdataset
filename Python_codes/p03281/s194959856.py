#!/usr/bin/env python3
def main():
    N = int(input())

    ans = 0
    for n in range(1, N + 1, 2):
        cnt = 0
        for divisor in range(1, N + 1):
            cnt += 0 if n % divisor else 1
        ans += 1 if cnt == 8 else 0
    print(ans)


if __name__ == '__main__':
    main()
