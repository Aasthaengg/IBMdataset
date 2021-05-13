# -*- coding: utf-8 -*-

def main():

    r, D, x = map(int, input().split())
    ans = []

    for i in range(10):
        x = r * x - D
        ans.append(x)

    for i in ans:
        print(i)


if __name__ == "__main__":
    main()