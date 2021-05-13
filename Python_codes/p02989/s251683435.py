# -*- coding: utf-8 -*-

def main():

    N = int(input())
    d = list(map(int, input().split()))

    d.sort()

    ans = d[N // 2] - d[N // 2 - 1]

    print(ans)


if __name__ == "__main__":
    main()