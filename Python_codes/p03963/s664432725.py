# -*- coding: utf-8 -*-

def main():

    N, K = map(int, input().split())
    ans = 1

    for i in range(N):
        if i == 0:
            ans *= K

        else:
            ans *= (K-1)

    print(ans)


if __name__ == "__main__":
    main()