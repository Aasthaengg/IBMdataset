#!/usr/bin/env python3
def main():
    _ = int(input())
    X = [int(x) for x in input().split()]

    ans = 10 ** 6
    for i in range(1, 101):
        res = 0
        for x in X:
            res += (x - i) ** 2
        ans = min(ans, res)
    print(ans)


if __name__ == '__main__':
    main()
