# -*- coding: utf-8 -*-

def main():

    N, K = map(int, input().split())
    S = input()

    ans = list(S)
    ans[K - 1] = S[K - 1].lower()

    ans = ''.join(ans)

    print(ans)


if __name__ == "__main__":
    main()