# -*- coding: utf-8 -*-

def main():

    W, H, x, y = map(int, input().split())

    ans = []

    if x == W / 2 and y == H / 2:
        ans.append(W * H / 2)
        ans.append(1)

    else:
        ans.append(W * H / 2)
        ans.append(0)

    print(ans[0], ans[1])


if __name__ == "__main__":
    main()