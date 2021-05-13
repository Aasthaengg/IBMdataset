# -*- coding: utf-8 -*-

def main():
   
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    ans = 0

    for i in range(1, N+1):
        if i <= K:
            ans += X

        else:
            ans += Y

    print(ans)


if __name__ == "__main__":
    main()