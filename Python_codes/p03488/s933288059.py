import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    x, y = map(int, readline().split())
    sx, sy = 0, 0

    for i in range(len(s)):
        if s[i] == "F":
            sx += 1
        else:
            break

    is_x = False
    cur = 0

    x_list = []
    y_list = []

    for i in range(sx + 1, len(s)):
        if s[i] == "F":
            cur += 1
        if s[i] == "T" or i == len(s) - 1:
            if is_x:
                x_list.append(cur)
            else:
                y_list.append(cur)
            cur = 0
            is_x = not is_x

    x_possible = set()
    x_possible.add(0)

    while x_list:
        x_possible_new = set()
        cx = x_list.pop()
        for px in x_possible:
            x_possible_new.add(px + cx)
            x_possible_new.add(px - cx)
        x_possible = x_possible_new

    y_possible = set()
    y_possible.add(0)

    while y_list:
        y_possible_new = set()
        cy = y_list.pop()
        for py in y_possible:
            y_possible_new.add(py + cy)
            y_possible_new.add(py - cy)
        y_possible = y_possible_new

    nx = x - sx
    ny = y

    if (nx in x_possible) and (ny in y_possible):
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()
