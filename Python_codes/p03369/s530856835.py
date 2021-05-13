# -*- coding: utf-8 -*-

def main():

    S = input()

    ans = 700

    for i in S:
        if i == 'o':
            ans += 100

    print(ans)


if __name__ == "__main__":
    main()