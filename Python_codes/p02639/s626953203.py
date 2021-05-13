# -*- coding: utf-8 -*-

def main():

    x = list(map(int, input().split()))
    n = len(x)

    for i in range(n):
        if i + 1 != x[i]:
            ans = i + 1
            break

    print(ans)


if __name__ == "__main__":
    main()