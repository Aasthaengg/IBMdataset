# -*- coding: utf-8 -*-

def main():

    A, B, C, D = map(int, input().split())

    area = []

    area.append(A * B)
    area.append(C * D)

    ans = max(area)

    print(ans)


if __name__ == "__main__":
    main()