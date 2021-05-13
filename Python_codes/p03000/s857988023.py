# -*- coding: utf-8 -*-

def main():

    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    D = 0
    ans = 0

    if D <= X:
        ans += 1

    for i in L:
        D += i
        if D <= X:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()