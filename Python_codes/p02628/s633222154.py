# -*- coding: utf-8 -*-

def main():

    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    ans = 0

    p.sort()
    

    for i in range(K):
        ans += p[i]

    print(ans)


if __name__ == "__main__":
    main()