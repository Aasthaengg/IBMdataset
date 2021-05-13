# -*- coding: utf-8 -*-

def main():

    a, b, c = map(int, input().split())

    color = {a, b, c}

    ans = len(color)

    print(ans)


if __name__ == "__main__":
    main()