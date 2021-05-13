# -*- coding: utf-8 -*-

def main():

    P, Q, R = map(int, input().split())

    path = [P, Q, R]

    path.sort()

    ans = path[0] + path[1]

    print(ans)


if __name__ == "__main__":
    main()