#!/usr/bin/env python3
def main():
    L = int(input())

    ans = 0
    for i in range(min(L, 1000)):
        for j in range(1000):
            a = i + (j / 1000)
            b = (L - a) / 2
            ans = max(ans, a * b * b)
    print(ans)


if __name__ == '__main__':
    main()
